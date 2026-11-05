# Roadmap

The step-by-step plan for this project: what gets built, in what order, and how we know each step is done.

The "why" behind each choice lives in [`docs/decisions/`](decisions/). This file only says what comes next. Update the status when a step finishes.

## What we are building

Among credit card customers who are late in a given month, predict who will catch up the next month. Then decide what to do with each one (no contact, SMS or call) and show the result in a dashboard that a non-scientist can understand.

## The type of model

**Binary classification.** The target has two classes:

| Class | Meaning |
|---|---|
| 1 | The customer was late in month t and caught up in month t+1 |
| 0 | The customer was late in month t and did not catch up in month t+1 |

The test is what the target looks like. A yes or no target is classification. A quantity, such as how much the customer will pay, would be regression.

The model does not stop at yes or no. It outputs a probability between 0 and 1, called the propensity, and the treatment policy uses that number.

Logistic regression, the baseline, is a classification model despite its name. It calculates a score and converts it into a probability.

## Steps

| # | Date | Step | Done when | Status |
|---|---|---|---|---|
| 1 | Nov 5 | Repository, agent files, decision log and git hook | A commit without the trailer is rejected, and the `record-decision` skill works in Pi | In progress: skill not yet tested in Pi |
| 2 | Nov 6 | Download the data, define the population and the target | Statuses 0 and -2 are checked in the data, decision 001 is confirmed or changed, and we know how many customers are late each month and how many catch up | To do |
| 3 | Nov 7 | Exploration: what separates customers who catch up | Each finding has a chart in `reports/figures/` | To do |
| 4 | Nov 8 | Features in SQL (DuckDB) | One row per customer and month, with current and maximum delay, bill trend, share of the bill paid and consecutive months late, and nothing from month t+1 | To do |
| 5 | Nov 9 | Time-based split and logistic regression | Trained on the earlier months, tested on the latest month, with the baseline AUC recorded | To do |
| 6 | Nov 10 | LightGBM with class imbalance handled | Compared with the baseline on the same test month | To do |
| 7 | Nov 11 | CatBoost and simple tuning, plus a checkpoint | Compared with LightGBM, final model chosen, and schedule reviewed: cut scope only if the first week ran very late | To do |
| 8 | Nov 12 | Evaluation: AUC, KS, calibration and gain by decile | All four are recorded for the chosen model, with charts | To do |
| 9 | Nov 13 | Explanation with SHAP | One chart for the whole model and one for a single customer | To do |
| 10 | Nov 14 | Treatment policy | Customers ranked by propensity × amount due, channel chosen by expected value, and contact costs and effects kept in one place as assumptions | To do |
| 11 | Nov 15 | Compare with a rule based on days late, and write the A/B plan | Offline comparison recorded, and the A/B plan written | To do |
| 12 | Nov 16 | Score API (FastAPI, Docker) and drift check (PSI) | The API returns a score from a Docker container, and PSI runs on a sample | To do |
| 13 | Nov 17 | Dashboard: portfolio and propensity bands | Both views work in Streamlit | To do |
| 14 | Nov 18 | Dashboard: why each customer got their score, and how much the policy recovers | Both views work in Streamlit | To do |
| 15 | Nov 19 | Skills: data analysis, new dashboard chart, explain a decision | Each skill was used at least once in Pi | To do |
| 16 | Nov 20 | README | It tells the story, the decisions and the results, and states the assumptions openly | To do |
| 17 | Nov 21 | Presentation and outside review | `scripts/build_presentation.py` generates it from the decisions, and a reviewer has given feedback | To do |
| 18 | Nov 22 | Final fixes and publish | Repository public and up to date, and no credentials or forbidden content in it | To do |

## Only if there is time left

These do not delay the steps above.

| Idea | What it adds | Depends on |
|---|---|---|
| Precision and recall by count and by amount | Shows whether the model finds the money and not only the customers | Step 8, plus a chosen cutoff |
| Correct the calibration with a second light model | Makes the probability closer to the real chance, which the policy multiplies by the amount due | Step 8 showing distortion, plus one month of data set aside for it |
