"""SDK-free host for the portable contract."""
from ..portable import AgentState, PortableAgent, StateStore


class LocalAdapter:
    async def run(self, agent: PortableAgent, state: AgentState,
                  *, store: StateStore | None = None) -> AgentState:
        return await agent.run(AgentState.from_json(state.to_json()), store=store)
