import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# STEP 1: Load the Excel file
file_path = r"C:\Users\chira\Desktop\data analytics project\machine_failure_analysis.xlsx"  # Apni actual file ka naam daal yaha
xls = pd.ExcelFile(file_path)

# STEP 2: Read all sheets into separate DataFrames
df_failure_count = pd.read_excel(xls, "Failure_count")  
df_failures_by_type = pd.read_excel(xls, "Failures_by_MachineType")
df_avg_temp_error = pd.read_excel(xls, "AvgTemp_ErrorRate")
df_failed_machines = pd.read_excel(xls, "Failed_machines")
df_max_usage_no_fail = pd.read_excel(xls, "MaxUsage_before_Failure")



# 🔹 1. FAILURE RATE BY MACHINE TYPE
plt.figure(figsize=(8, 5))
sns.barplot(x='Machine_Type', y='Failures', data=df_failures_by_type, palette='viridis')
plt.title("Failure Rate by Machine Type")
plt.xlabel("Machine Type")
plt.ylabel("Failure Count")
plt.xticks(rotation=45)
plt.show()

# 🔹 2. FAILURE VS. USAGE HOURS
plt.figure(figsize=(8, 5))
sns.boxplot(x='Failure', y='Usage_Hours', data=df_failed_machines, palette='coolwarm')
plt.title("Failure vs. Usage Hours")
plt.xlabel("Failure (0 = No, 1 = Yes)")
plt.ylabel("Usage Hours")
plt.show()

# 🔹 3. FAILURE VS. TEMPERATURE
plt.figure(figsize=(8, 5))
sns.boxplot(x='Failure', y='Temperature_C', data=df_failed_machines, palette='magma')
plt.title("Failure vs. Temperature")
plt.xlabel("Failure (0 = No, 1 = Yes)")
plt.ylabel("Temperature (°C)")
plt.show()

# 🔹 4. FAILURE VS. ERROR RATE
plt.figure(figsize=(8, 5))
sns.boxplot(x='Failure', y='Error_Rate', data=df_failed_machines, palette='crest')
plt.title("Failure vs. Error Rate")
plt.xlabel("Failure (0 = No, 1 = Yes)")
plt.ylabel("Error Rate")
plt.show()
