# propensity-to-pay

A credit card collections project. Among customers who are late in a given month, it predicts who will catch up next month, decides what to do with each one (no contact, SMS or call) and shows the result in a dashboard that a non-scientist can understand.

## Working with Rafael

- Talk to Rafael in Brazilian Portuguese. Code, docs and commit messages are in English.
- This is Rafael's first machine learning project, and he has to be able to defend every choice in a presentation. Explain what a step does and why before doing it, in plain terms and with a small example.
- Rafael makes the decisions. Propose options with a recommendation, and never pick silently.
- Keep it simple. Choose what can be explained over what scores slightly higher.

## The project, in order

1. **Data:** "Default of Credit Card Clients" (UCI). Define the population (customers late in month t) and the target (caught up in t+1). Confirm that the columns allow this before building on it.
2. **Exploration:** what separates customers who catch up from those who don't. Each finding gets a chart.
3. **Features in SQL (DuckDB):** current and maximum delay, bill trend, share of the bill paid, consecutive months late.
4. **Baseline:** time-based split and logistic regression.
5. **Models:** LightGBM against the baseline, with class imbalance handled, then CatBoost and simple tuning.
6. **Evaluation:** AUC, KS, calibration and gain by decile.
7. **Explanation:** SHAP, for the model and for each customer.
8. **Treatment policy:** rank by propensity × amount due, choose the channel by expected value (recovery − contact cost) and compare offline with a rule based on days late. Write an A/B plan for production.
9. **Serving:** a FastAPI score API with Docker, and a drift check (PSI).
10. **Dashboard (Streamlit):** the portfolio, propensity bands, why each customer got their score, and how much the policy recovers.

The dataset does not say what happens when a customer is contacted. Contact costs and effects are **assumptions**: keep them in one place and state them openly in the README.

## Decision log

Every decision goes in `docs/decisions/NNN-short-name.md` when it is made, not later:

```markdown
# NNN: The decision, in one line
Question: what we needed to answer
Options: what was considered
Choice: what was picked
Why: the reason, with the number that supports it
Evidence: reports/figures/NNN-name.png
Decided by: rafael | agent
For the presentation: yes | no
```

- `Decided by: rafael` only when Rafael made the call. If you proposed it and he only accepted without discussing it, write `agent`, and flag it so he can study it.
- Read `docs/decisions/` before changing anything: don't redo or contradict what was already decided.
- Save every chart that supports a decision in `reports/figures/`.

## Commits

A hook in `.githooks/` rejects any commit that touches code or notebooks without a trailer:

```
Decision: 007
```

Use `Decision: none` when no decision was made. Don't bypass the hook.

## What must never enter this repository

Credentials, data from any company, and the names of employers, people or job applications.
