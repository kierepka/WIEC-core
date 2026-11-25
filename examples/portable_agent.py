"""Run a single offline agent unchanged on local, ADK or Microsoft hosts."""
import argparse
import asyncio
from pathlib import Path

from wiec import Evidence
from wiec.portable import AgentManifest, AgentRequest, EvidenceEchoBackend, JsonStateStore, PortableAgent


async def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--platform", choices=("local", "adk", "microsoft"), default="local")
    parser.add_argument("--state-dir", type=Path, default=Path(".wiec-state"))
    parser.add_argument("--run-id", default="portable-demo")
    parser.add_argument("--resume", action="store_true", help="Load an existing checkpoint")
    args = parser.parse_args()
    if args.platform == "adk":
        from wiec.adapters.google_adk import GoogleAdkAdapter
        host = GoogleAdkAdapter()
    elif args.platform == "microsoft":
        from wiec.adapters.microsoft import MicrosoftAdapter
        host = MicrosoftAdapter()
    else:
        from wiec.adapters.local import LocalAdapter
        host = LocalAdapter()
    agent = PortableAgent(AgentManifest("source_analyst", "v1", "evidence_echo_v1"), EvidenceEchoBackend())
    store = JsonStateStore(args.state_dir)
    if not args.resume and (args.state_dir / f"{args.run_id}.json").exists():
        parser.error("Checkpoint exists; use --resume or a new --run-id")
    state = store.load(args.run_id) if args.resume else agent.prepare(AgentRequest(
        run_id=args.run_id, question="Which source positions must remain visible?",
        evidence=(Evidence("s1", "fixture:position-a", "Method A may help."),
                  Evidence("s2", "fixture:position-b", "Method A may not help.")),
    ))
    result = await host.run(agent, state, store=store)
    print(result.to_json())
    if result.status != "completed":
        raise SystemExit(1)


if __name__ == "__main__":
    asyncio.run(main())
