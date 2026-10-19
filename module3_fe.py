import pandas as pd

data = {
    "student_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "join_date": ["2026-01-15", "2026-02-20", "2026-03-05", "2026-03-28",
                  "2026-04-10", "2026-05-18", "2026-06-02", "2026-07-21"],
    "age": [17, 18, 19, 18, 22, 25, 20, 31],
    "city": ["Jaipur", "Delhi", "Jaipur", "Pune", "Delhi", "Pune", "Jaipur", "Delhi"],
    "marks": [45, 78, 62, 90, 55, 70, 85, 40],
    "study_hours": [2, 6, 4, 8, 3, 5, 7, 2],
    "level": ["Low", "High", "Medium", "High", "Low", "Medium", "High", "Low"],
    "passed": [0, 1, 1, 1, 0, 1, 1, 0],
}

df = pd.DataFrame(data)

# ---- Technique 1: Date features ----
df["join_date"] = pd.to_datetime(df["join_date"])
df["join_month"] = df["join_date"].dt.month
df["join_weekday"] = df["join_date"].dt.dayofweek   # Monday = 0

# ---- Technique 2: Derived feature (ratio) ----
df["marks_per_hour"] = df["marks"] / df["study_hours"]

# ---- Technique 3: Binning ----
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 18, 22, 100],
    labels=["teen", "young", "adult"],
)

print(df[["join_date", "join_month", "join_weekday",
          "marks_per_hour", "age", "age_group"]])

#-------------------------------------------------------------

df = pd.DataFrame({
    "city": ["Jaipur", "Delhi", "Pune", "Delhi"],
    "level": ["Low", "High", "Medium", "Low"],
})

# Ordinal: level (order hai)
level_map = {"Low": 0, "Medium": 1, "High": 2}
df["level_encoded"] = df["level"].map(level_map)

# One-hot: city (order nahi)
df = pd.get_dummies(df, columns=["city"], dtype=int)

print(df)