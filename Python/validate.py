import pandas as pd

patients = pd.read_csv("../data/patients.csv", keep_default_na=False)
doctors = pd.read_csv("../data/doctors.csv", keep_default_na=False)
admissions = pd.read_csv("../data/admissions.csv", keep_default_na=False)
vitals = pd.read_csv("../data/vitals.csv", keep_default_na=False)
treatments = pd.read_csv("../data/treatments.csv", keep_default_na=False)

tables = {
    "Patients": patients,
    "Doctors": doctors,
    "Admissions": admissions,
    "Vitals": vitals,
    "Treatments": treatments
}

for name, df in tables.items():
    print(f"\n{name}")
    total_nulls = df.isnull().sum().sum()
    print(f"Total Null Values: {total_nulls}")

print("\nPRIMARY KEY DUPLICATES")

print(
    "Duplicate Patient IDs:",
    patients["patient_id"].duplicated().sum()
)

print(
    "Duplicate Doctor IDs:",
    doctors["doctor_id"].duplicated().sum()
)

print(
    "Duplicate Admission IDs:",
    admissions["admission_id"].duplicated().sum()
)

print(
    "Duplicate Vital IDs:",
    vitals["vital_id"].duplicated().sum()
)

print(
    "Duplicate Treatment IDs:",
    treatments["treatment_id"].duplicated().sum()
)

print("\nFOREIGN KEY VALIDATION")

invalid_patient_fk = (
    ~admissions["patient_id"]
    .isin(patients["patient_id"])
).sum()

print(
    "Invalid Patient IDs in Admissions:",
    invalid_patient_fk
)

invalid_doctor_fk = (
    ~admissions["doctor_id"]
    .isin(doctors["doctor_id"])
).sum()

print(
    "Invalid Doctor IDs in Admissions:",
    invalid_doctor_fk
)

invalid_vitals_fk = (
    ~vitals["admission_id"]
    .isin(admissions["admission_id"])
).sum()

print(
    "Invalid Admission IDs in Vitals:",
    invalid_vitals_fk
)

invalid_treatment_fk = (
    ~treatments["admission_id"]
    .isin(admissions["admission_id"])
).sum()

print(
    "Invalid Admission IDs in Treatments:",
    invalid_treatment_fk
)

print("\nValidation Completed")