import pytest
from wiec import (
    ActionKind, Challenge, Claim, Council, Evidence,
    ProposedAction, SafetyPolicy, Verdict,
)


def test_missing_action_denied():
    assert SafetyPolicy().evaluate(None).verdict is Verdict.DENY


def test_read_only_allowed():
    action = ProposedAction("a", "agent", ActionKind.READ_ONLY, "local analysis")
    assert SafetyPolicy().evaluate(action).verdict is Verdict.ALLOW


def test_external_write_denied_without_review():
    action = ProposedAction("a", "agent", ActionKind.EXTERNAL_WRITE, "send message")
    assert SafetyPolicy().evaluate(action).verdict is Verdict.DENY


def test_external_write_denied_even_with_review_and_approval():
    action = ProposedAction("a", "agent", ActionKind.EXTERNAL_WRITE, "send message", True, True)
    assert SafetyPolicy().evaluate(action).verdict is Verdict.DENY


def test_physical_action_denied():
    action = ProposedAction("a", "agent", ActionKind.PHYSICAL, "move actuator", True, True)
    assert SafetyPolicy().evaluate(action).verdict is Verdict.DENY


def test_contradictory_claims_retained():
    claims = [Claim("c1", "a", "X"), Claim("c2", "b", "not X")]
    result = Council().synthesize(claims, [Challenge("h", "c1", "b", "conflict")], [])
    assert len(result.claims) == 2
    assert len(result.challenges) == 1
    assert result.disagreements_preserved
    assert not result.verified_truth


def test_invalid_evidence_reference_rejected():
    with pytest.raises(ValueError):
        Council().synthesize([Claim("c", "a", "X", ("missing",))], [], [])


def test_unknown_challenge_reference_rejected():
    with pytest.raises(ValueError):
        Council().synthesize([], [Challenge("h", "missing", "a", "reason")], [])
