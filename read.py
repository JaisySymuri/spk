import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load data
df = pd.read_csv("students.csv")

# Target
df["pass"] = (df["exam_score"] >= 60).astype(int)

X = df.drop(columns=["student_id", "exam_score", "pass"])
y = df["pass"]

# Column types
categorical = ["gender", "course", "study_method"]
binary = ["internet_access"]
ordinal = ["sleep_quality", "facility_rating", "exam_difficulty"]
numeric = ["age", "study_hours", "class_attendance", "sleep_hours"]

ordinal_categories = [
    ["poor", "average", "good"],
    ["low", "medium", "high"],
    ["easy", "moderate", "hard"],
]

# Preprocessing
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
    ("bin", OneHotEncoder(drop="if_binary", handle_unknown="ignore"), binary),
    ("ord", OrdinalEncoder(categories=ordinal_categories), ordinal),
    ("num", "passthrough", numeric)
])

model = Pipeline([
    ("prep", preprocessor),
    ("clf", LogisticRegression(max_iter=1000))
])

model.fit(X, y)
