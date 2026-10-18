import pandas as pd

df = pd.read_csv("students.csv")   # load the CSV into a DataFrame

print(df.head())          # first 5 rows: "what does the data look like?"
print(df.shape)           # (rows, columns)
print(df.columns)         # all column names
print(df.dtypes)          # data type of each column
df.info()                 # types + non-null counts (spot missing values here)
print(df.describe())      # mean, std, min, max for numeric columns
print(df.isnull().sum())  # missing values per column
print(df.duplicated().sum())  # number of fully duplicate rows

print(df["age"])                          # one column (a Series)
print(df[["name", "study_hours"]])        # multiple columns (note double brackets)
print(df[df["attendance_pct"] > 80])      # filter rows by a condition
print(df[(df["city"] == "Udaipur") & (df["passed"] == 1)])  # two conditions: use & and ()
print(df["city"].value_counts())          # count of each category