import pandas as pd

df= pd.read_csv("students.csv")

#print(df.head())

#print(df.shape)

#print(df.columns)

#print(df.dtypes)

#df.info()

#print(df.describe())

#print(df.isnull().sum())

#print(df.duplicated().sum())

print(df["age"])                          # one column (a Series)
print(df[["name", "study_hours"]])        # multiple columns (note double brackets)
print(df[df["attendance_pct"] > 80])      # filter rows by a condition
print(df[(df["city"] == "Udaipur") & (df["passed"] == 1)])  # two conditions: use & and ()
print(df["city"].value_counts())          # count of each category