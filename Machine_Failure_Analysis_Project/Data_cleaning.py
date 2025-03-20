import pandas as pd

# Load the Excel file
file_path = r"C:\Users\chira\Desktop\data analytics project\machine_failure_analysis.xlsx"
xls = pd.ExcelFile(file_path)

# Load each sheet into a separate DataFrame
df_failure_count = pd.read_excel(xls, "Failure_count")
df_failures_by_type = pd.read_excel(xls, "Failures_by_MachineType")
df_avg_temp_error = pd.read_excel(xls, "AvgTemp_ErrorRate")
df_failed_machines = pd.read_excel(xls, "Failed_machines")
df_max_usage_no_fail = pd.read_excel(xls, "MaxUsage_before_Failure")

# Display basic info about each dataset
dfs = [df_failure_count, df_failures_by_type, df_avg_temp_error, df_failed_machines, df_max_usage_no_fail]
df_names = ["Failure Count", "Failures by Machine Type", "Avg Temp & Error Rate", "Failed Machines", "Max Usage Before Failure"]

for name, df in zip(df_names, dfs):
    print(f"\n{name} Dataset:")
    print(df.info())  # Shows column types & missing values
    print(df.head())  # Displays first 5 rows


import pandas as pd

# Load the Excel file
file_path = r"C:\Users\chira\Desktop\data analytics project\machine_failure_analysis.xlsx"
xls = pd.ExcelFile(file_path)

# Load only the "Failed Machines" dataset for cleaning
df_failed_machines = pd.read_excel(xls, "Failed_machines")

# ✅ 1. Check for duplicates
duplicates = df_failed_machines.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# ✅ 2. Check for outliers (Temperature, Usage Hours, Error Rate)
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12,5))

# Boxplot for Temperature
plt.subplot(1,3,1)
sns.boxplot(y=df_failed_machines["Temperature_C"])
plt.title("Temperature Outliers")

# Boxplot for Usage Hours
plt.subplot(1,3,2)
sns.boxplot(y=df_failed_machines["Usage_Hours"])
plt.title("Usage Hours Outliers")

# Boxplot for Error Rate
plt.subplot(1,3,3)
sns.boxplot(y=df_failed_machines["Error_Rate"])
plt.title("Error Rate Outliers")

plt.tight_layout()
plt.show()

# ✅ 3. Standardize column names (remove spaces, lowercase)
df_failed_machines.columns = df_failed_machines.columns.str.lower().str.replace(" ", "_")
print("\nUpdated Column Names:", df_failed_machines.columns)
