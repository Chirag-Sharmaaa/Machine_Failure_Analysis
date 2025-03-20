CREATE DATABASE predictive_maintenance;
USE predictive_maintenance;
CREATE TABLE machine_data (
    Machine_ID INT PRIMARY KEY,
    Machine_Type VARCHAR(50),
    Usage_Hours INT,
    Temperature_C FLOAT,
    Error_Rate FLOAT,
    Maintenance_History INT,
    Failure INT
);

SELECT * FROM machine_data LIMIT 10;

SELECT Failure, COUNT(*) AS Count 
FROM machine_data 
GROUP BY Failure;

SELECT Machine_Type, COUNT(*) AS Failures
FROM machine_data
WHERE Failure = 1
GROUP BY Machine_Type
ORDER BY Failures DESC;

SELECT 
    AVG(Temperature_C) AS Avg_Temperature_Failed,
    AVG(Error_Rate) AS Avg_Error_Rate_Failed
FROM machine_data
WHERE Failure = 1;

SELECT *
FROM machine_data
WHERE Failure = 1 AND Maintenance_History > 5;

SELECT Machine_Type, MAX(Usage_Hours) AS Max_Usage_No_Failure
FROM machine_data
WHERE Failure = 0
GROUP BY Machine_Type;




