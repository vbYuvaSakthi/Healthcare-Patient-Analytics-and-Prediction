import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

patients = pd.read_csv("../data/cleaned_patients.csv")
admissions = pd.read_csv("../data/cleaned_admissions.csv")
vitals = pd.read_csv("../data/cleaned_vitals.csv")

patients["dob"] = pd.to_datetime(patients["dob"])
admissions["admission_date"] = pd.to_datetime(admissions["admission_date"])

patients["age"] = (
    (pd.Timestamp.today() - patients["dob"]).dt.days // 365
)

admissions = admissions.sort_values(
    ["patient_id", "admission_date"]
)

admissions["next_admission"] = admissions.groupby(
    "patient_id"
)["admission_date"].shift(-1)

admissions["days_between"] = (
    admissions["next_admission"]
    - admissions["admission_date"]
).dt.days

admissions["readmitted"] = np.where(
    admissions["days_between"] <= 30,
    1,
    0
)

admissions["readmitted"] = admissions["readmitted"].fillna(0)

visit_count = admissions.groupby(
    "patient_id"
).size().reset_index(name="past_visits")

patients = patients.merge(
    visit_count,
    on="patient_id",
    how="left"
)

vital_summary = vitals.groupby(
    "admission_id"
).agg({
    "heart_rate":"mean",
    "oxygen_level":"mean",
    "temperature":"mean"
}).reset_index()

data = admissions.merge(
    patients[
        [
            "patient_id",
            "age",
            "gender",
            "chronic_conditions",
            "past_visits"
        ]
    ],
    on="patient_id",
    how="left"
)

data = data.merge(
    vital_summary,
    on="admission_id",
    how="left"
)

le = LabelEncoder()

data["gender"] = le.fit_transform(
    data["gender"]
)

data["chronic_conditions"] = (
    data["chronic_conditions"]
    .fillna("None")
    .apply(lambda x: 0 if x == "None" else len(str(x).split(",")))
)

X = data[
    [
        "age",
        "gender",
        "past_visits",
        "heart_rate",
        "oxygen_level",
        "temperature",
        "chronic_conditions"
    ]
]

y = data["readmitted"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight='balanced'
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report")
print(
    classification_report(
        y_test,
        predictions
    )
)


importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop Risk Factors")
print(importance)

data["risk_score"] = model.predict_proba(X)[:,1]

data["risk_level"] = np.where(
    data["risk_score"] >= 0.70,
    "High",
    np.where(
        data["risk_score"] >= 0.40,
        "Medium",
        "Low"
    )
)

risk_table = data[
    [
        "admission_id",
        "patient_id",
        "risk_score",
        "risk_level"
    ]
]

risk_table.to_csv(
    "../data/readmission_risk.csv",
    index=False
)

print("\nreadmission_risk.csv created successfully")