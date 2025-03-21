# Machine Failure Analysis

## 📌 Project Overview
This project focuses on **Machine Failure Analysis** using **Descriptive Analytics**. We aim to analyze a dataset containing machine sensor readings and failure records to uncover insights about different failure types, their frequency, and possible contributing factors.

Using **SQL, Python, and Excel**, we performed **data cleaning, exploratory data analysis (EDA), and dashboard visualization** to derive meaningful insights from the dataset.

---

## 📂 Files in This Repository

| File Name                       | Description |
|---------------------------------|-------------|
| `Predictive_Maintenance_Data.csv` | The dataset used for analysis. |
| `Machine_failure_queries.sql`            | SQL queries used for data exploration and insights. |
| `Data_cleaning.py`               | Python script for cleaning the dataset. |
| `EDA.py`                         | Python script for Exploratory Data Analysis (EDA). |
| `Machine_Failure_Analysis.xlsx`  | Excel file containing cleaned data, SQL output, and a final dashboard. |
| `Dashboard.png`       | Screenshot of the final dashboard created in Excel. |

---

## 🛠️ Tech Stack Used

- **SQL (MySQL/PostgreSQL)** → For querying and extracting insights from data.
- **Python (Pandas, Matplotlib, Seaborn)** → For data cleaning and EDA.
- **Excel (Pivot Tables & Charts)** → For final dashboard visualization.

---

## 🔍 Data Cleaning & Preprocessing

- Removed irrelevant and redundant columns.
- Handled missing values by imputing or removing where necessary.
- Converted timestamps into a readable format.
- Standardized categorical values for better analysis.

---

## 📊 Exploratory Data Analysis (EDA)

EDA helped us understand **failure patterns and sensor behavior**. Some key insights:

1️⃣ **Failure Frequency Analysis** – We identified the most common types of failures.
2️⃣ **Sensor Trends** – We analyzed how temperature, pressure, and other sensor readings vary before failure.
3️⃣ **Correlation Study** – We checked if specific conditions lead to frequent failures.


![img1](https://github.com/Chirag-Sharmaaa/Machine_Failure_Analysis/blob/main/Machine_Failure_Analysis_Project/failure%20rate%20by%20machine%20type.png)
![img2](https://github.com/Chirag-Sharmaaa/Machine_Failure_Analysis/blob/main/Machine_Failure_Analysis_Project/failure%20vs%20error%20rate.png)
![img3](https://github.com/Chirag-Sharmaaa/Machine_Failure_Analysis/blob/main/Machine_Failure_Analysis_Project/failure%20vs%20temp.png)
![img4](https://github.com/Chirag-Sharmaaa/Machine_Failure_Analysis/blob/main/Machine_Failure_Analysis_Project/failure%20vs%20usage%20hours.png)

---

## 📈 Dashboard in Excel

The final dashboard was created using **Pivot Tables & Charts** to summarize:

- Failure distribution across different failure types.
- Monthly trends of failures.
- Sensor values leading to failure events.

 ![img5](https://github.com/Chirag-Sharmaaa/Machine_Failure_Analysis/blob/main/Machine_Failure_Analysis_Project/Dashboard.png)

---

## 📝 SQL Queries Used

Some key SQL queries included:

```sql
-- SELECT Failure, COUNT(*) AS Count 
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
```


---

## 📌 Conclusion
This **Machine Failure Analysis** project helped us:

✔ Identify key failure trends.  
✔ Understand the impact of different sensor readings.  
✔ Visualize results through SQL, Python, and Excel dashboards.  

By analyzing historical machine failures, we can make better data-driven decisions for **preventive maintenance strategies**.

---

## 📎 How to Use This Repo

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/machine-failure-analysis.git
   ```
2. Run SQL queries using MySQL/PostgreSQL.
3. Execute Python scripts for data cleaning & EDA.
4. Open the Excel file to view the dashboard.

🚀 **Feel free to explore and contribute!**

