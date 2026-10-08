import pandas as pd

patients = pd.read_csv("../data/patients.csv", keep_default_na=False)
doctors = pd.read_csv("../data/doctors.csv", keep_default_na=False)
admissions = pd.read_csv("../data/admissions.csv", keep_default_na=False)
vitals = pd.read_csv("../data/vitals.csv", keep_default_na=False)
treatments = pd.read_csv("../data/treatments.csv", keep_default_na=False)

patients = patients.drop_duplicates()

patients["dob"] = pd.to_datetime(
    patients["dob"],
    errors="coerce"
)

patients["address"] = (
    patients["address"]
    .fillna("Unknown")
    .replace("", "Unknown")
)

patients["chronic_conditions"] = (
    patients["chronic_conditions"]
    .replace("", "None")
    .fillna("None")
)

patients["chronic_conditions"] = patients["chronic_conditions"].astype(str)

patients["chronic_conditions"] = (
    patients["chronic_conditions"]
    .replace("nan", "None")
)

doctors = doctors.drop_duplicates()

admissions = admissions.drop_duplicates()

admissions["admission_date"] = pd.to_datetime(
    admissions["admission_date"],
    errors="coerce"
)

admissions["discharge_date"] = pd.to_datetime(
    admissions["discharge_date"],
    errors="coerce"
)

admissions["room_no"] = admissions["room_no"].fillna("Not Assigned")

vitals = vitals.drop_duplicates()

vitals["recorded_time"] = pd.to_datetime(
    vitals["recorded_time"],
    errors="coerce"
)

vitals["temperature"] = vitals["temperature"].fillna(
    vitals["temperature"].mean()
)

treatments = treatments.drop_duplicates()

treatments["treatment_date"] = pd.to_datetime(
    treatments["treatment_date"],
    errors="coerce"
)

treatments["procedure"] = treatments["procedure"].fillna("Not Specified")
treatments["dosage"] = treatments["dosage"].fillna("Not Specified")

patients.to_csv("../data/cleaned_patients.csv", index=False)
doctors.to_csv("../data/cleaned_doctors.csv", index=False)
admissions.to_csv("../data/cleaned_admissions.csv", index=False)
vitals.to_csv("../data/cleaned_vitals.csv", index=False)
treatments.to_csv("../data/cleaned_treatments.csv", index=False)

print("Transformation Completed Successfully")