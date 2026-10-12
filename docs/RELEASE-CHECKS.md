# Release preparation checks

Prepared on 2026-10-12 for version 0.1.0.

- Both JavaScript files pass Node.js syntax checks (not a Cinnamon runtime test).
- Metadata and settings schema parse as JSON; UUID and instance settings match the source.
- All five applet files are byte-identical to the source and the prepared Spices release in the original TaskbarMenu project.
- The existing local official Cinnamon Spices `validate-spice` script passes on the original, identical Spices package. The standalone repository intentionally uses a different layout.
- Installation and update copy operations were exercised in a temporary home directory.
- README shell blocks pass `bash -n`.
- The installable ZIP was extracted and its applet files compared to the source.
- The original icon and promotional graphic are unchanged. The graphic depicts an earlier dialog and is labelled historical.
- Existing JavaScript headers, the original specification, and the original release README all declare GPL version 3. The full GPL-3 text was copied from `/usr/share/common-licenses/GPL-3`.
- No separately attributed third-party code was found in the supplied files. External code and artwork provenance could not be independently established.
- The original TaskbarMenu checkout was clean and has not been modified. The cinnamon-spices-applets checkout already contained unrelated local changes; none were altered by this work. PR 8942 has not been modified.

Not completed: interactive testing under Cinnamon, authenticated verification of repository ownership/existence, GitHub creation/upload, and release publication. Publication requires the owner's explicit approval and an authenticated GitHub connection.
