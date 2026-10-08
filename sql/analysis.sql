#Total Patients
SELECT COUNT(*) AS Total_Patients
FROM dim_patients;

#Total Admissions
SELECT COUNT(*) AS Total_Admissions
FROM fact_admissions;

#Total Doctors
SELECT COUNT(*) AS Total_Doctors
FROM dim_doctors;

#Admissions by Diagnosis
SELECT
    diagnosis,
    COUNT(*) AS Total_Admissions
FROM fact_admissions
GROUP BY diagnosis
ORDER BY Total_Admissions DESC;

# Admissions by Doctor
SELECT
    CONCAT(d.first_name,' ',d.last_name) AS Doctor_Name,
    COUNT(a.admission_id) AS Total_Admissions
FROM fact_admissions a
JOIN dim_doctors d
ON a.doctor_id = d.doctor_id
GROUP BY Doctor_Name
ORDER BY Total_Admissions DESC;

#Average Patient Age
SELECT
AVG(TIMESTAMPDIFF(YEAR,dob,CURDATE())) AS Average_Age
FROM dim_patients;

#Gender Distribution
SELECT
    gender,
    COUNT(*) AS Total_Patients
FROM dim_patients
GROUP BY gender;

#Patients With Chronic Conditions
SELECT
    chronic_conditions,
    COUNT(*) AS Patient_Count
FROM dim_patients
GROUP BY chronic_conditions
ORDER BY Patient_Count DESC;

#Average Heart Rate
SELECT
ROUND(AVG(heart_rate),2) AS Average_Heart_Rate
FROM fact_vitals;

#Average Oxygen Level
SELECT
ROUND(AVG(oxygen_level),2) AS Average_Oxygen_Level
FROM fact_vitals;

#Average Temperature
SELECT
ROUND(AVG(temperature),2) AS Average_Temperature
FROM fact_vitals;

#Patients with Low Oxygen (<95)
SELECT
COUNT(*) AS Critical_Patients
FROM fact_vitals
WHERE oxygen_level < 95;

#Most Common Treatments
SELECT
medication,
COUNT(*) AS Usage_Count
FROM fact_treatments
GROUP BY medication
ORDER BY Usage_Count DESC;

#Most Common Procedures
SELECT
    `procedure`,
    COUNT(*) AS Procedure_Count
FROM fact_treatments
GROUP BY `procedure`
ORDER BY Procedure_Count DESC;

#Average Length of Stay
SELECT
ROUND(
AVG(
DATEDIFF(discharge_date, admission_date)
),2
) AS Avg_Length_Of_Stay
FROM fact_admissions
WHERE discharge_date IS NOT NULL;

#Monthly Admission Trend
SELECT
YEAR(admission_date) AS Year,
MONTH(admission_date) AS Month,
COUNT(*) AS Total_Admissions
FROM fact_admissions
GROUP BY Year, Month
ORDER BY Year, Month;

#Admissions by Specialization
SELECT
d.specialization,
COUNT(a.admission_id) AS Total_Admissions
FROM fact_admissions a
JOIN dim_doctors d
ON a.doctor_id = d.doctor_id
GROUP BY d.specialization
ORDER BY Total_Admissions DESC;

#Complete Hospital Summary Query
SELECT
(SELECT COUNT(*) FROM dim_patients) AS Total_Patients,
(SELECT COUNT(*) FROM dim_doctors) AS Total_Doctors,
(SELECT COUNT(*) FROM fact_admissions) AS Total_Admissions,
(SELECT COUNT(*) FROM fact_treatments) AS Total_Treatments,
(SELECT COUNT(*) FROM fact_vitals) AS Total_Vitals;