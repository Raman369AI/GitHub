# Databricks notebook source
dbutils.fs.mount(source = "wasbs://projectle@leproject.blob.core.windows.net/",
                 mount_point ='/mnt/ptr',
                 extra_configs={'fs.azure.account.key.leproject.blob.core.windows.net':'LypsAbnvR5/yeTJXl2CS93nj2Bah0JbrrQOa7QFihkuavqhhYJojNJY3G8DkjgnEK+SiK7uXdFwB+AStuK5Mkg=='})

# COMMAND ----------

dbutils.fs.ls('/mnt/ptr/all')

# COMMAND ----------

df = spark.read.csv("/mnt/ptr/all/raw.csv", header=True, inferSchema=True)

# COMMAND ----------

dbutils.fs.ls('/mnt/ptr/transformed/')

# COMMAND ----------

df.describe()

# COMMAND ----------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Descriptive Statistics
desc_stats = df.describe()



# COMMAND ----------

# Checking for Missing Values
missing_values = df.isnull().sum()

# COMMAND ----------

# Data Visualizations
# Distribution of 'Life expectancy'
plt.figure(figsize=(10, 6))
sns.histplot(df['Life expectancy '], kde=True)
plt.title('Distribution of Life Expectancy')
plt.xlabel('Life Expectancy')
plt.ylabel('Frequency')
plt.show()



# COMMAND ----------

# Boxplot for 'Life expectancy' by 'Status' (Developed vs Developing)
plt.figure(figsize=(10, 6))
sns.boxplot(x='Status', y='Life expectancy ', data=data)
plt.title('Life Expectancy by Country Status')
plt.xlabel('Status')
plt.ylabel('Life Expectancy')
plt.show()




# COMMAND ----------

# Correlation Analysis
correlation_matrix = df.corr()
plt.figure(figsize=(15, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Variables')
plt.show()

# COMMAND ----------

desc_stats, missing_values

# COMMAND ----------

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Handling missing values
data_clean = df.dropna()

# Selecting relevant features for the regression model
# Excluding 'Country' and 'Year' as they are not numerical, and 'Status' as it's categorical
features = data_clean.drop(['Country', 'Year', 'Status', 'Life expectancy '], axis=1)
target = data_clean['Life expectancy ']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Creating a Linear Regression model
model = LinearRegression()

# Fitting the model
model.fit(X_train, y_train)

# Predicting life expectancy
predictions = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

mse, r2

# COMMAND ----------

spark_df = spark.createDataFrame(df)

# COMMAND ----------

spark_df.write.option("header",'true').csv("/mnt/ptr/transformed/final")
