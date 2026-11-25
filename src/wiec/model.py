from dataclasses import dataclass
from enum import Enum


class ActionKind(str, Enum):
    READ_ONLY = "read_only"
    EXTERNAL_WRITE = "external_write"
    PHYSICAL = "physical"


class Verdict(str, Enum):
    ALLOW = "allow"
    DENY = "deny"
    SAFE_STOP = "safe_stop"


@dataclass(frozen=True)
class Evidence:
    id: str
    source: str
    description: str


@dataclass(frozen=True)
class Claim:
    id: str
    agent_id: str
    statement: str
    evidence_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class Challenge:
    id: str
    claim_id: str
    challenger_id: str
    reason: str


@dataclass(frozen=True)
class ProposedAction:
    id: str
    agent_id: str
    kind: ActionKind
    description: str
    risk_reviewed: bool = False
    approved_by_human: bool = False


@dataclass(frozen=True)
class SafetyDecision:
    verdict: Verdict
    reason: str
