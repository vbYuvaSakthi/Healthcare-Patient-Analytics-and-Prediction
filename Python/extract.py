import pandas as pd

patients = pd.read_csv("../data/patients.csv")
doctors = pd.read_csv("../data/doctors.csv")
admissions = pd.read_csv("../data/admissions.csv")
vitals = pd.read_csv("../data/vitals.csv")
treatments = pd.read_csv("../data/treatments.csv")

datasets = {
    "Patients": patients,
    "Doctors": doctors,
    "Admissions": admissions,
    "Vitals": vitals,
    "Treatments": treatments
}

for name, df in datasets.items():

    print(f"{name} TABLE")

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumn Names:")
    for col in df.columns:
        print(col)
