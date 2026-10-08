#dim patients
CREATE TABLE Dim_Patients (
    patient_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    dob DATE,
    gender VARCHAR(10),
    contact_no BIGINT,
    address VARCHAR(255),
    chronic_conditions VARCHAR(255)
);

#dim doctors
CREATE TABLE Dim_Doctors (
    doctor_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    specialization VARCHAR(100),
    contact_no BIGINT
);




