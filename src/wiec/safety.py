from .model import ActionKind, ProposedAction, SafetyDecision, Verdict


class SafetyPolicy:
    """Demonstration policy only; NOT a security boundary."""

    def evaluate(self, action: ProposedAction | None) -> SafetyDecision:
        if action is None:
            return SafetyDecision(Verdict.DENY, "Missing action")
        if action.kind is ActionKind.READ_ONLY:
            return SafetyDecision(Verdict.ALLOW, "No external side effects declared")
        if not action.risk_reviewed:
            return SafetyDecision(Verdict.DENY, "Risk review required")
        if not action.approved_by_human:
            return SafetyDecision(Verdict.DENY, "Human approval required")
        # Even approved external actions remain blocked until a real
        # enforcement boundary and domain-specific policies exist.
        return SafetyDecision(Verdict.DENY, "External execution not implemented")
