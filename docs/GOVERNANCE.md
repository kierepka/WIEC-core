# Governance and decision process

Status: initial project process; no independent review board is established.

## Authority and review

Repository maintainers control merges and releases. Contributors propose changes
through issues and pull requests. A future Research Council can advise but cannot
merge code, change policy or approve its own permissions by agreement.
Maintainership and safety authority are separate operational roles in the target
deployment; the current repository does not establish that organizational separation.

Behavioral changes need a concrete acceptance case. Changes to action policy,
data access or quantum execution require a threat-model update and review by
someone other than the author. If no independent reviewer is available, keep the
change a proposal/draft; do not describe it as independently reviewed.

## Architecture decisions

ADRs state context, status, choice, alternatives, consequences and validation gate.
“Proposed” is not implementation approval. Supersede decisions explicitly and
link the replacement. Keep source evidence separate from project preferences.
Public roadmap items have no implied delivery date or funding commitment.

## Scientific reporting

Publish negative results, failed replications, limitations and relevant dependencies.
Do not imply model/provider independence from different names alone. Disclose
evaluation conditions and conflicts when making comparative claims. Preserve
minority interpretations that remain supported in scope.

## Community conduct

Critique arguments and implementations respectfully. Do not harass, expose private
information or misrepresent contributors. Report conduct concerns privately to an
available maintainer contact listed in their public profile; no private moderation
channel is configured by this document. Public issues should contain only safe,
non-sensitive project discussion.

## Licensing and identity

Project code and original repository documentation use Apache-2.0 unless a file
explicitly states otherwise. Linked external papers and vendor docs retain their
own rights. Adding a link does not relicense its contents. WIEC's Polish expansion
and English translation are defined in [START_PL.md](START_PL.md); trademark
clearance remains uncompleted and no trademark rights are granted by the license.
