from wiec import Claim, Challenge, Council, ProposedAction, ActionKind, SafetyPolicy

result = Council().synthesize(
    [Claim("1", "perspective-a", "Hypothesis A"),
     Claim("2", "perspective-b", "Alternative to A")],
    [Challenge("3", "1", "perspective-b", "Evidence is insufficient")],
    [],
)
print("Claims retained:", len(result.claims))
print("Truth verified:", result.verified_truth)
proposal = ProposedAction("4", "perspective-a", ActionKind.EXTERNAL_WRITE, "publish")
print("Publication decision:", SafetyPolicy().evaluate(proposal))
