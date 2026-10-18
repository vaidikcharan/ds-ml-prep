import pandas as pd

#Q1. students.csv load karo.
df= pd.read_csv("students.csv")

#Q2. age ki median, study_hours ki mean, aur city ki mode print karo.
print(df["age"].median())
print(df["study_hours"].mean())
print(df["city"].mode())

#Q3. Teeno columns ke missing values bharo
#(age, study_hours: median se; city: mode se).

df["age"]= df["age"].fillna(df["age"].median())
df["study_hours"]= df["study_hours"].fillna(df["study_hours"].median())
df["city"]= df["city"].fillna(df["city"].mode()[0])

#Q4. Duplicate row hatao.

df= df.drop_duplicates()

#Q5. df.isnull().sum() aur df.shape print karo

print(df.isnull().sum())
print(df.shape)