import pandas as pd

# Practice CSV banao (sirf ek baar)
data = {
    "student_id": [1, 2, 3, 4, 5, 6],
    "age": [17, 18, 19, None, 22, 25],
    "city": ["Jaipur", "Delhi", "Pune", "Delhi", "Jaipur", "Pune"],
    "marks": [45, 78, 62, 90, 55, 70],
    "study_hours": [2, 6, 4, 8, 3, 5],
    "passed": [0, 1, 1, 1, 0, 1],
}
pd.DataFrame(data).to_csv("students.csv", index=False)

# Ab EDA shuru: CSV padho
df = pd.read_csv("students.csv")

print("SHAPE:", df.shape)
print("\nHEAD:")
print(df.head())
print("\nINFO:")
df.info()
print("\nDESCRIBE:")
print(df.describe())

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nMISSING AGE WALI ROW:")
print(df[df["age"].isnull()])

print("\ncity kitni baar ayi:")
print(df["city"].value_counts())

print("\n Pass ya fail: ")
print(df["passed"].value_counts())

import matplotlib.pyplot as plt

plt.hist(df["marks"], bins=5)
plt.title("Marks ka distribution")
plt.xlabel("Marks")
plt.ylabel("Students ki ginti")
plt.show()

plt.hist(df["study_hours"], bins=5)
plt.title("study hours os students")
plt.xlabel("Students ki ginti")
plt.ylabel("marks")
plt.show()