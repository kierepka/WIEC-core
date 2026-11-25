from dataclasses import dataclass
from .model import Claim, Challenge, Evidence


@dataclass(frozen=True)
class CouncilResult:
    claims: tuple[Claim, ...]
    challenges: tuple[Challenge, ...]
    evidence: tuple[Evidence, ...]
    verified_truth: bool = False

    @property
    def disagreements_preserved(self) -> bool:
        return True


class Council:
    """Retains conflicting claims; never infers truth from agreement."""

    def synthesize(
        self,
        claims: list[Claim],
        challenges: list[Challenge],
        evidence: list[Evidence],
    ) -> CouncilResult:
        ids = {c.id for c in claims}
        if len(ids) != len(claims):
            raise ValueError("Duplicate claim id")
        evidence_ids = {e.id for e in evidence}
        if len(evidence_ids) != len(evidence):
            raise ValueError("Duplicate evidence id")
        if any(c.claim_id not in ids for c in challenges):
            raise ValueError("Challenge references unknown claim")
        if any(set(c.evidence_ids) - evidence_ids for c in claims):
            raise ValueError("Claim references unknown evidence")
        return CouncilResult(tuple(claims), tuple(challenges), tuple(evidence))
