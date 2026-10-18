import pandas as pd

df= pd.read_csv("students.csv")

#1. How many students have attendance_pct below 70?
low= df[df["attendance_pct"] < 70]
print(low)
print(len(low))


#2. What is the average study_hours of students who passed? 
# (Hint: filter first, then .mean())
stds_passed= df[df["passed"] == 1]
print(stds_passed["study_hours"].mean())


#3. Which column(s) have missing values, and how many each?
print(df.isnull().sum())


#4. Which student row is duplicated?
print(df[df.duplicated()])