import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV File
df = pd.read_csv('data.csv')

# Display Dataset
print(df)

# Calculate Average Salary
average_salary = df['Salary'].mean()
print("Average Salary:", average_salary)

# ---------------- BAR CHART ----------------
plt.figure(figsize=(8,5))
plt.bar(df['Name'], df['Salary'])
plt.title('Salary of Employees')
plt.xlabel('Employee Name')
plt.ylabel('Salary')
plt.show()

# ---------------- SCATTER PLOT ----------------
plt.figure(figsize=(8,5))
plt.scatter(df['Experience'], df['Salary'])
plt.title('Experience vs Salary')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()

# ---------------- HEATMAP ----------------
plt.figure(figsize=(6,4))

correlation = df[['Age', 'Salary', 'Experience']].corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm')

plt.title('Correlation Heatmap')

plt.show()