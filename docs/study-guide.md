# Study guide

What to watch before each step of the [roadmap](roadmap.md). This is a first machine learning project, so every step starts with understanding the concepts and only then moves on to building.

## How each step works

1. **Watch.** Look up the concepts for the step and watch a video on each one you don't know yet.
2. **Ask.** Bring the questions back to the conversation, and clear them up with a small example.
3. **Build.** Do the step, with each new term explained when it comes up.
4. **Explain back.** Before closing the step, say in your own words what was done and why. If that doesn't work yet, the step isn't finished.

A new term that shows up along the way gets added to this file, in the step where it appeared.

**Finding videos:** paste the search term into YouTube. Add "em português" to find videos in Portuguese. StatQuest is a good channel for the statistics and modeling terms.

## The stack

| Tool | What it does in this project | Search for |
|---|---|---|
| Jupyter | A notebook that mixes code, charts and notes | jupyter notebook tutorial for beginners |
| pandas | Works with tables of data in Python | pandas tutorial for beginners |
| NumPy | Fast math on lists of numbers, used underneath pandas | numpy tutorial for beginners |
| Matplotlib | Draws the charts | matplotlib tutorial for beginners |
| DuckDB | Runs SQL on local files, with no server | duckdb tutorial python |
| scikit-learn | Logistic regression, data splitting and metrics | scikit-learn tutorial for beginners |
| LightGBM | A gradient boosting model | lightgbm explained |
| CatBoost | Another gradient boosting model | catboost explained |
| SHAP | Explains why the model gave each score | shap values explained |
| FastAPI | Serves the score through an API | fastapi tutorial for beginners |
| Docker | Packages the API so it runs anywhere | docker tutorial for beginners |
| Streamlit | Builds the dashboard in Python | streamlit tutorial for beginners |

## Before each step

Step 1 (repository and decision log) needs no videos, since it doesn't involve data science.

### Step 2: Data, population and target

| Concept | In plain words | Search for |
|---|---|---|
| Supervised learning | Learning from past cases where the answer is known | supervised learning explained |
| Classification vs regression | Predicting a category vs predicting a quantity | classification vs regression machine learning |
| Target and features | The answer to predict, and the information used to predict it | features and target machine learning |

### Step 3: Exploration

| Concept | In plain words | Search for |
|---|---|---|
| Exploratory data analysis | Looking at the data before modeling it | exploratory data analysis pandas |
| Mean, median and percentiles | Different ways to describe the typical value and the spread | mean median percentile explained |
| Histogram and distribution | How the values are spread out | histograms clearly explained |
| Correlation | How much two values move together | correlation clearly explained |
| Class imbalance | One answer is much more common than the other | class imbalance machine learning |

### Step 4: Features in SQL

| Concept | In plain words | Search for |
|---|---|---|
| Feature engineering | Building useful columns from the raw data | feature engineering explained |
| Window functions | SQL that looks at neighboring rows, such as the previous month | sql window functions tutorial |
| Data leakage | Using information the model wouldn't have at prediction time, which makes results look better than they are | data leakage machine learning |

### Step 5: Split and logistic regression

| Concept | In plain words | Search for |
|---|---|---|
| Train and test sets | Learn on one part of the data and grade on another | train test split explained |
| Time-based split | Train on the past and test on the future, as in real use | time based split machine learning |
| Overfitting | Memorizing the training data instead of learning from it | overfitting explained |
| Baseline | A simple model that better ones have to beat | baseline model machine learning |
| Logistic regression | A classification model that outputs a probability | logistic regression clearly explained |
| Logit and sigmoid | The raw score, and the function that turns it into 0 to 1 | sigmoid function logit explained |

### Step 6: LightGBM

| Concept | In plain words | Search for |
|---|---|---|
| Decision tree | A chain of yes or no questions | decision trees clearly explained |
| Gradient boosting | Many small trees, each one correcting the errors of the previous ones | gradient boost clearly explained |
| Class weights | Making the rarer class count more during training | class weights imbalanced data |

### Step 7: CatBoost and tuning

| Concept | In plain words | Search for |
|---|---|---|
| Hyperparameters | Model settings chosen before training | hyperparameter tuning explained |
| Validation set | A third slice of data for choosing settings, leaving the test set untouched | train validation test explained |

### Step 8: Evaluation

| Concept | In plain words | Search for |
|---|---|---|
| Confusion matrix | A count of the right and wrong answers of each kind | confusion matrix explained |
| Precision and recall | Of those flagged, how many were right; of those that mattered, how many were found | precision and recall explained |
| ROC and AUC | How well the model ranks positives above negatives | roc and auc clearly explained |
| KS statistic | The largest gap between the score distributions of the two classes, common in credit | ks statistic credit scoring |
| Calibration | Whether customers scored 80% really catch up about 80% of the time | probability calibration explained |
| Gain by decile | How much of the result sits in the top 10%, 20% and so on of the scores | gain and lift chart explained |

### Step 9: SHAP

| Concept | In plain words | Search for |
|---|---|---|
| Feature importance | Which columns matter most to the model | feature importance explained |
| SHAP values | How much each column pushed one customer's score up or down | shap values explained |

### Steps 10 and 11: Treatment policy and comparison

| Concept | In plain words | Search for |
|---|---|---|
| Propensity model | A model that gives the chance of someone taking an action | propensity model explained |
| Expected value | Chance × amount, minus the cost | expected value explained |
| A/B test | Compare two treatments on randomly split groups | a/b testing explained |
| Statistical significance | Whether a difference is likely to be more than chance | statistical significance explained |
| Champion and challenger | The current approach against a candidate to replace it | champion challenger model |

### Step 12: API and drift

| Concept | In plain words | Search for |
|---|---|---|
| Model serving | Making a trained model available to other systems | machine learning model deployment fastapi |
| Data drift | New data starts to look different from the training data | data drift explained |
| PSI | A number that measures how much a distribution has shifted | population stability index explained |

### Steps 13 to 18: Dashboard, README and presentation

| Concept | In plain words | Search for |
|---|---|---|
| Data storytelling | Presenting results so that a non-specialist can follow | data storytelling explained |

## If there is time left

| Concept | In plain words | Search for |
|---|---|---|
| Platt scaling and isotonic regression | Two ways to correct calibration with a second light model | platt scaling isotonic regression explained |
| Weighted metrics | Metrics where each case counts by its amount and not as one | sample weight precision recall |
