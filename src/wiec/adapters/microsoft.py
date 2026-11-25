"""Native Microsoft Agent Framework host, with no model service or tools."""
from ..portable import AgentState, ContractError, PortableAgent, StateStore


def make_microsoft_agent(agent: PortableAgent, *, store: StateStore | None = None):
    """Create a BaseAgent exposing the portable invocation through SDK messages.

    Only non-streaming, single-envelope calls are supported. WIEC checkpoints,
    rather than vendor conversation history, are the authoritative state.
    """
    try:
        from agent_framework import BaseAgent, AgentResponse, Message
    except ModuleNotFoundError as exc:
        raise ImportError("Install wiec-core[microsoft] to use Microsoft Agent Framework") from exc

    class WiecMicrosoftAgent(BaseAgent):
        def run(self, messages=None, *, stream=False, session=None,
                function_invocation_kwargs=None, client_kwargs=None):
            if stream:
                raise NotImplementedError("WIEC portable host supports non-streaming calls only")
            if function_invocation_kwargs or client_kwargs:
                raise ContractError("Provider/tool arguments are unsupported")

            async def invoke():
                if not isinstance(messages, (list, tuple)) or len(messages) != 1:
                    raise ContractError("Microsoft host expects one user message")
                message = messages[0]
                if not isinstance(message, Message) or message.role != "user":
                    raise ContractError("Microsoft host expects a user Message")
                if len(message.contents) != 1 or message.contents[0].type != "text":
                    raise ContractError("Microsoft host expects one text content")
                state = AgentState.from_json(message.text)
                result = await agent.run(state, store=store)
                return AgentResponse(
                    messages=[Message("assistant", [result.to_json()], author_name=self.name)],
                    agent_id=self.id, response_id=state.request.run_id,
                )

            return invoke()

    return WiecMicrosoftAgent(id=agent.manifest.agent_id, name="wiec_portable",
                             description="Bounded local WIEC agent")


class MicrosoftAdapter:
    async def run(self, agent: PortableAgent, state: AgentState,
                  *, store: StateStore | None = None) -> AgentState:
        native = make_microsoft_agent(agent, store=store)
        from agent_framework import Message
        response = await native.run([Message("user", [state.to_json()])],
                                    session=native.create_session())
        result = AgentState.from_json(response.text)
        if result.manifest != state.manifest or result.request != state.request:
            raise ContractError("Microsoft result identity mismatch")
        return result
