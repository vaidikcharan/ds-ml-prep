import pandas as pd 
import numpy as np

df= pd.read_csv("students.csv")

df.loc[3, ["attendance_pct"]]= 500

print(df["attendance_pct"].describe())
print(df[df["attendance_pct"] > 100])

df.loc[df["attendance_pct"] > 100, "attendance_pct"]= np.nan
df["attendance_pct"]= df["attendance_pct"].fillna(df["attendance_pct"].median())
print(df["attendance_pct"].describe())

