# Telco Customer Churn — Data Preparation and Visualization

Holberton School Modern AI exercises for exploring, cleaning, visualizing, engineering, and preparing Telco customer data for machine learning.

## Requirements

Python 3, pandas, NumPy, Matplotlib, seaborn, SciPy, and scikit-learn.

```bash
python3 -m pip install pandas numpy matplotlib seaborn scipy scikit-learn
```

## Dataset and file names

Place the original `Telco-Customer-Churn.csv` in this directory. The original CSV is **not tracked in this repository**; obtain the dataset from your course materials. The first five tasks use the original CSV.

After converting, cleaning, deduplicating and dropping `customerID`, save the cleaned data as **`precleaned-Telco-Customer-Churn.csv`**. Subsequent tasks expect exactly this spelling.

```python
import pandas as pd
convert_columns = __import__('2-convert_columns').convert_columns
clean_total_charges = __import__('3-clean_total_charges').clean_total_charges
remove_duplicates = __import__('4-remove_duplicates').remove_duplicates
drop_customerID = __import__('5-drop_customerID').drop_customerID

df = pd.read_csv('Telco-Customer-Churn.csv')
df = convert_columns(df)
df = clean_total_charges(df)
df = remove_duplicates(df)
df = drop_customerID(df)
df.to_csv('precleaned-Telco-Customer-Churn.csv', index=False)
```

## Tasks

| Task | File | Purpose |
| --- | --- | --- |
| 0 | `0-describe_data.py` | Inspect shape, types, first rows, nulls and duplicates |
| 1 | `1-plot_missingness.py` | Visualize missing entries by row and column |
| 2 | `2-convert_columns.py` | Convert charges to numeric and senior status to Yes/No |
| 3 | `3-clean_total_charges.py` | Drop, median-fill or tenure-based impute missing charges |
| 4 | `4-remove_duplicates.py` | Deduplicate records |
| 5 | `5-drop_customerID.py` | Remove identifier column |
| 6 | `6-plot_churn_distribution.py` | Chart Churn category counts |
| 7 | `7-plot_categorical_distributions.py` | Chart categorical features |
| 8 | `8-plot_continuous_distributions.py` | Histograms, KDE and boxplots |
| 9 | `9-plot_correlation_heatmap.py` | Annotated numeric correlation matrix |
| 10 | `10-plot_categorical_vs_churn.py` | Churn rate per category |
| 11 | `11-plot_numeric_vs_churn.py` | Numeric distributions by Churn |
| 12 | `12-chi_square_tests.py` | Chi-square categorical feature tests |
| 13 | `13-ttest_numeric.py` | Welch t-tests of numeric features |
| 14 | `14-create_features.py` | Build NumServices and TenureGroup |
| 15 | `15-encode_features.py` | Label, ordinal and one-hot encoding |
| 16 | `16-scale_numeric.py` | Standardize monthly and total charges |
| 17 | `17-split_data.py` | Stratified train/test split |

## Example: prepare data for ML

```python
import pandas as pd
create_features = __import__('14-create_features').create_features
encode_features = __import__('15-encode_features').encode_features
scale_numeric = __import__('16-scale_numeric').scale_numeric
split_data = __import__('17-split_data').split_data

df = pd.read_csv('precleaned-Telco-Customer-Churn.csv')
df = df.drop(columns=['gender', 'PhoneService'])
df = create_features(df)
encoded, churn_le, binary_oe, tenure_oe = encode_features(df)
scaled = scale_numeric(encoded)
X_train, X_test, y_train, y_test = split_data(scaled)
print(X_train.shape, X_test.shape)
```

## Expected course dataset observations

The provided assignment shows 7,043 raw records, 11 blank strings in `TotalCharges`, and 7,032 records after the default drop cleaning. For a stratified 80/20 split, the expected feature shapes are `(5625, 13)` and `(1407, 13)`; these values have not been independently verified against the original CSV in this environment.

## Validation and caveats

- Python syntax checks passed for the 16 newly prepared task files.
- A representative synthetic-data pipeline test passed for cleaning, feature creation, encoders, scaling, splitting, statistical tests, and plotting.
- The original CSV and exact reference plots were unavailable, so the full-dataset numeric output and exact pixel-level appearance were not verified.
- The assignment requests encoding and scaling before splitting. In a production ML pipeline, fit encoders/scalers on the training data only to prevent data leakage.
- `TotalCharges` values containing whitespace become NaN after `pd.to_numeric(..., errors='coerce')`. With the default `drop` method, rows with missing charges are removed.
- Task 14 intentionally excludes `PhoneService` from the service count and excludes customers at tenure 0 from `TenureGroup` bins.
