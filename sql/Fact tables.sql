#fact admissions
CREATE TABLE Fact_Admissions (
    admission_id INT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    admission_date DATE,
    discharge_date DATE,
    diagnosis VARCHAR(255),
    room_no VARCHAR(20),

    FOREIGN KEY (patient_id)
    REFERENCES Dim_Patients(patient_id),

    FOREIGN KEY (doctor_id)
    REFERENCES Dim_Doctors(doctor_id)
);

#fact vitals
CREATE TABLE Fact_Vitals (
    vital_id INT PRIMARY KEY,
    admission_id INT,
    recorded_time DATETIME,
    heart_rate INT,
    blood_pressure VARCHAR(20),
    oxygen_level INT,
    temperature DECIMAL(5,2),

    FOREIGN KEY (admission_id)
    REFERENCES Fact_Admissions(admission_id)
);

#fact treatments
CREATE TABLE Fact_Treatments (
    treatment_id INT PRIMARY KEY,
    admission_id INT,
    treatment_date DATE,
    `procedure` VARCHAR(255),
    medication VARCHAR(255),
    dosage VARCHAR(100),

    FOREIGN KEY (admission_id)
    REFERENCES Fact_Admissions(admission_id)
);



