# Security policy

This is an experimental prototype. **Do not connect it to production systems,
medical devices, financial accounts, or privileged external tools.**

## Initial threats
Prompt injection; tool authorization bypass; forged evidence; coordinated
agent agreement; malicious plugins; policy tampering; audit log modification;
unsafe shutdown; and harm from omission.

## Reporting
Use GitHub's private vulnerability reporting if enabled for this repository;
otherwise use an available maintainer contact on their public GitHub profile.
Do not post credentials, private source content or exploitable deployment details
in public issues. No dedicated private reporting channel is configured by this file.

## Boundaries
Current policy is in-process and can be bypassed by code running with the
same privileges. It provides testable application behavior, not isolation.

The [target threat model](docs/SAFETY.md) covers prompt injection, forged approval,
gateway bypass, replay, budget exhaustion and remote quantum submissions. It is
a design, not a claim of enforced isolation in the current release.
