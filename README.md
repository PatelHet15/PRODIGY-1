# PRODIGY-1
Data Visualization of Dataset of Ages

Population Data Analysis
This repository contains the analysis of population data focusing on the percentage of the population ages 0-14 in different economies. The analysis includes data cleaning, visualization, correlation analysis, and statistical tests.

Data
The dataset used in this analysis contains information about the population ages 0-14 as a percentage of the total population for various economies in the year 2022. The data is read from a CSV file named population.csv.

Dependencies
The following Python libraries are required to run the analysis:

pandas
matplotlib
seaborn
numpy
scipy

You can install the required libraries using:
pip install pandas matplotlib seaborn numpy scipy

Steps in Analysis:-

1.Data Reading and Initial Exploration:
  -Read the data from the CSV file.
  - Display the shape, columns, info, and description of the data.

2.Data Cleaning:
  -Handle missing values by dropping rows with any missing data.
  -
3.Data Visualization:
  -Countplot: Visualize the count of economies.
  -Boxplot: Show the distribution of the population ages 0-14 by economy.
  -Scatterplot: Plot the relationship between economies and the population ages 0-14.
  -Barplot: Display the mean population ages 0-14 by economy.
  -Violinplot: Show the distribution and density of the population ages 0-14 by economy.

4.Correlation Analysis:
  -Compute and display the correlation matrix of the dataset.
  -Visualize the correlation matrix using a heatmap.

5.Statistical Analysis:
  -Perform T-tests between each pair of economies to compare the population ages 0-14 percentages.

Results:-

 -Visualizations: 
   -Different types of plots provide insights into the distribution of population ages 0-14 across various economies.
Correlation Matrix: Shows the correlation between different variables in the dataset.
   -T-tests: Provides statistical comparisons between the population ages 0-14 percentages of different economies.
 -License
   -This project is licensed under the MIT License.
