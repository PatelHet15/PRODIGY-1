import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read the data from the CSV file
data = pd.read_csv('population.csv')

# Data Cleaning and Preprocessing
print("Data Shape:", data.shape)
print("Data Columns:", data.columns)
print("Data Info:", data.info())
print("Data Description:", data.describe())

# Handling Missing Values
data.dropna(inplace=True)

# Data Visualization
plt.figure(figsize=(10, 6))
sns.countplot(x='Economy', data=data)
plt.title('Count of Economies')
plt.xlabel('Economy')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Economy', y='Population ages 0-14 (% of total population)', data=data)
plt.title('Boxplot of Population Ages 0-14 by Economy')
plt.xlabel('Economy')
plt.ylabel('Population Ages 0-14 (% of total population)')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Economy', y='Population ages 0-14 (% of total population)', data=data)
plt.title('Scatterplot of Population Ages 0-14 by Economy')
plt.xlabel('Economy')
plt.ylabel('Population Ages 0-14 (% of total population)')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='Economy', y='Population ages 0-14 (% of total population)', data=data)
plt.title('Barplot of Population Ages 0-14 by Economy')
plt.xlabel('Economy')
plt.ylabel('Population Ages 0-14 (% of total population)')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(10, 6))
sns.violinplot(x='Economy', y='Population ages 0-14 (% of total population)', data=data)
plt.title('Violinplot of Population Ages 0-14 by Economy')
plt.xlabel('Economy')
plt.ylabel('Population Ages 0-14 (% of total population)')
plt.xticks(rotation=90)
plt.show()

# Correlation Analysis
corr_matrix = data.corr()
print("Correlation Matrix:")
print(corr_matrix)

# Heatmap of Correlation Matrix
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Heatmap of Correlation Matrix')
plt.show()

# Statistical Analysis
from scipy.stats import ttest_ind

economies = data['Economy'].unique()
for i in range(len(economies)):
    for j in range(i+1, len(economies)):
        economy1 = economies[i]
        economy2 = economies[j]
        data1 = data[data['Economy'] == economy1]['Population ages 0-14 (% of total population)']
        data2 = data[data['Economy'] == economy2]['Population ages 0-14 (% of total population)']
        t_stat, p_val = ttest_ind(data1, data2)
        print(f"T-test between {economy1} and {economy2}: t-stat={t_stat:.2f}, p-val={p_val:.2f}")