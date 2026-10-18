<div align="center">

# 🧠 DS-ML-Prep

### From raw CSV to working ML model, one module at a time.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerics-013243?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Coming%20Soon-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Learning%20in%20Public-brightgreen?style=for-the-badge)

*A first-semester B.Tech CSE (AI/ML) student's hands-on journey to becoming competition-ready in Data Science & Machine Learning.*

</div>

---

## 🎯 What is this?

This repo is my **practice log** while preparing for a beginner-level Data Science / ML competition. Instead of just reading theory, I write code for every concept, break it, debug it, and push it here.

**Goal:** take an *unfamiliar* CSV dataset, clean it, engineer useful features, train a suitable model, evaluate it properly, and explain my solution under time pressure.

---

## 🗺️ Roadmap

| # | Module | Status |
|---|--------|--------|
| 1 | 📂 CSV & Pandas (load, inspect, select, filter) | ✅ Done |
| 2 | 🧹 Statistics & Data Cleaning (mean/median/mode, missing values, duplicates, outliers) | ✅ Exercises done |
| 3 | 🛠️ Feature Engineering (new features, dates, encoding, scaling) | ⏳ Next |
| 4 | 🤖 ML Essentials (train/test split, classification vs regression, metrics) | ⬜ Planned |
| 5 | 🏗️ End-to-end project with scikit-learn `Pipeline` | ⬜ Planned |
| 6 | 🚀 Deployment & Monitoring basics | ⬜ If time permits |
| 7 | ⏱️ Timed mock competition | ⬜ Planned |

---

## 📁 Repository Structure

```
ds-ml-prep/
├── module1.py        # Creates the practice dataset (students.csv)
├── exercise1.py      # Pandas inspection & filtering practice
├── exercise3.py      # Outlier / invalid value cleaning practice
├── students.csv      # Small, intentionally messy practice dataset
└── README.md
```

---

## 🧪 What I've Practiced So Far

**📂 Pandas basics**
- Loading data with `pd.read_csv()`
- Inspecting with `head()`, `shape`, `info()`, `describe()`, `dtypes`
- Selecting columns and filtering rows with conditions

**🧹 Data cleaning**
- Finding missing values with `isnull().sum()`
- Filling with **median** (numeric) and **mode** (categorical)
- Detecting and dropping duplicates
- Spotting **invalid values** (e.g. attendance > 100) and fixing them instead of blindly deleting rows

**📌 Lessons learned the hard way**
- `df["col"].fillna(...)` returns a new Series. Always assign it back.
- `.median` ≠ `.median()`. Missing parentheses silently break your data.
- ID and name columns are not features.
- Split first, then compute statistics from training data only (avoid **data leakage**).

---

## ⚡ Quick Start (Windows + VS Code)

```bash
# 1. Clone the repo
git clone https://github.com/vaidikcharan/ds-ml-prep.git
cd ds-ml-prep

# 2. Install dependencies
pip install pandas numpy scikit-learn matplotlib

# 3. Generate the practice dataset
python module1.py

# 4. Run an exercise
python exercise3.py
```

> If `python` isn't recognized, try `py` instead.

---

## 🧰 My Go-To Workflow for an Unfamiliar CSV

```text
1. Load        →  pd.read_csv()
2. Inspect     →  head(), shape, info(), describe(), isnull().sum(), duplicated().sum()
3. Find target →  what am I predicting? classification or regression?
4. Clean       →  fix types, invalid values, missing values, duplicates
5. Engineer    →  new features, dates, encoding, scaling
6. Split       →  train_test_split() BEFORE learning any statistics
7. Baseline    →  simple model first
8. Evaluate    →  right metric for the task (not just accuracy)
9. Improve     →  one or two sensible changes
10. Explain    →  what worked, what didn't, and why
```

---

## 📈 Progress Log

| Date | What I did |
|------|------------|
| 19 Oct 2026 | Module 1 + Module 2 exercises: pandas inspection, missing values, duplicates, outlier handling. First push to GitHub 🎉 |

---

## 🤝 Connect

Learning in public. Feedback, tips, and corrections are always welcome.

**GitHub:** [@vaidikcharan](https://github.com/vaidikcharan)

<div align="center">

⭐ *If this repo helps you start your own DS/ML journey, drop a star!* ⭐

</div>
