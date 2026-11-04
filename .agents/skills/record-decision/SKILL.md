---
name: record-decision
description: Records a project decision in docs/decisions/ in the AGENTS.md format, with the next number. Use as soon as a decision is made about data, features, models, evaluation, policy or serving.
---

# Record a decision

Write the decision when it is made, not later.

1. Read the files in `docs/decisions/`. Don't redo or contradict what was already decided. If the new decision replaces an old one, say so in `Why`.
2. Create the file with the next number. The script path is relative to this skill directory, and the short name uses lowercase letters, numbers and hyphens:

   ```bash
   python scripts/new_decision.py short-name
   ```

3. Fill in every field of the file the script printed:

   - **Title:** the decision, in one line.
   - **Question:** what we needed to answer.
   - **Options:** what was considered.
   - **Choice:** what was picked.
   - **Why:** the reason, with the number that supports it.
   - **Evidence:** the chart, saved as `reports/figures/NNN-name.png`. Write `none` if there is no chart yet, and say why.
   - **Decided by:** `rafael` only when Rafael made the call. If you proposed it and he only accepted without discussing it, write `agent`.
   - **For the presentation:** `yes` or `no`.

4. Show Rafael the result, in Brazilian Portuguese. If `Decided by` is `agent`, flag it so he can study it.
5. Commit code or notebooks that follow from this decision with the line `Decision: NNN` in the message.
