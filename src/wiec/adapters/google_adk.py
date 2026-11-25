"""Host the same WIEC agent inside a real Google ADK BaseAgent/Runner.

No LlmAgent, model API, credentials, remote tools or vendor memory is used.
"""
from uuid import uuid4

from ..portable import AgentState, ContractError, PortableAgent, StateStore


def make_adk_agent(agent: PortableAgent, *, store: StateStore | None = None):
    """Create an ADK-native custom agent accepting one WIEC checkpoint as text."""
    try:
        from google.adk.agents import BaseAgent
        from google.adk.events import Event
        from google.genai import types
    except ModuleNotFoundError as exc:
        raise ImportError("Install wiec-core[adk] to use Google ADK") from exc

    class WiecAdkAgent(BaseAgent):
        async def _run_async_impl(self, ctx):
            content = ctx.user_content
            parts = content.parts if content is not None else None
            if not parts or len(parts) != 1 or parts[0].text is None:
                raise ContractError("ADK expects one portable-state text part")
            state = AgentState.from_json(parts[0].text)
            result = await agent.run(state, store=store)
            yield Event(author=self.name, content=types.Content(
                role="model", parts=[types.Part(text=result.to_json())]
            ))

    return WiecAdkAgent(name="wiec_portable", description="Bounded local WIEC agent")


class GoogleAdkAdapter:
    async def run(self, agent: PortableAgent, state: AgentState,
                  *, store: StateStore | None = None) -> AgentState:
        native = make_adk_agent(agent, store=store)
        from google.adk.runners import Runner
        from google.adk.sessions import InMemorySessionService
        from google.genai import types

        # A fresh host session prevents platform history from changing WIEC input.
        service = InMemorySessionService()
        app_name, user_id, session_id = "wiec", "local", uuid4().hex
        await service.create_session(app_name=app_name, user_id=user_id, session_id=session_id)
        runner = Runner(app_name=app_name, agent=native, session_service=service)
        results = []
        try:
            async for event in runner.run_async(
                user_id=user_id, session_id=session_id,
                new_message=types.Content(role="user", parts=[types.Part(text=state.to_json())]),
            ):
                if event.author == native.name and event.content and not event.partial:
                    for part in event.content.parts or []:
                        if part.text:
                            results.append(AgentState.from_json(part.text))
        finally:
            await runner.close()
        if len(results) != 1:
            raise ContractError("Expected exactly one ADK portable result")
        result = results[0]
        if result.manifest != state.manifest or result.request != state.request:
            raise ContractError("ADK result identity mismatch")
        return result
