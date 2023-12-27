# -*- coding: utf-8 -*-
"""Sleep_Health_Analysis_inPython_MoumikSaha.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zY9P-_EJgNNBdqGcoWHU-4WIha7C3eME
"""

import pandas as pd #data loading and manupulation
import numpy as np # mathematical cal
import matplotlib.pyplot as plt #visualisation
import seaborn as sns #visualisation stats

data=pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
data.head() #to display the top 5 rows

data.shape #no of rows and columns

data.columns #to print the feature name or columns

data.columns.tolist()

data.info() #to give the information of no of rows, no of columns, in which column missing values is missing, datatypes,memory access

data.describe() #to show statistical summery (descriptive stats)

data.isna().sum() #check the missing values

data.duplicated().sum() #checking for duplicates values

data.Gender.value_counts() #Give the data of number of male and female

"""Description: Visualize the distribution of genders in the dataset."""

sns.countplot(x='Gender', data=data)
plt.show()

"""Description: distribution of ages in the dataset."""

sns.histplot(x='Age', data=data, bins=10, kde=True)
plt.show()

"""Description: The distribution of sleep durations."""

sns.histplot(x='Sleep Duration', data=data, bins=10, kde=True)
plt.show()

"""Description: Visualisation of the distribution of sleep quality."""

sns.countplot(x='Quality of Sleep', data=data)
plt.show()

"""Description: the correlation between daily steps and sleep duration."""

sns.scatterplot(x='Daily Steps', y='Sleep Duration', data=data)
plt.show()

"""Description: Visualize the distribution of sleep disorders."""

sns.countplot(x='Sleep Disorder', data=data)
plt.xticks(rotation=45)
plt.show()

"""Description: Explore the distribution of sleep disorders across different occupations."""

sns.countplot(x='Sleep Disorder', hue='Occupation', data=data)
plt.xticks(rotation=35)
plt.show()

"""Description: Explore the relationship between physical activity level and sleep duration."""

sns.boxplot(x='Physical Activity Level', y='Sleep Duration', data=data)
plt.show()

"""Description: Explore the relationship between daily steps and sleep duration based on gender."""

sns.scatterplot(x='Daily Steps', y='Sleep Duration', hue='Gender', data=data)
plt.show()

"""Description: Identify and visualize outliers indivisually in the daily steps column."""

sns.boxplot(x='Daily Steps', data=data)
plt.title("boxplot of Daily Steps")
plt.show()



"""Description: Identify and visualize outliers indivisually in the stress level column."""

sns.boxplot(x=data['Stress Level'])
plt.title("boxplot of Stress Level")
plt.show()

"""Description: Identify and visualize outliers of every Categorical column."""

int_cols = data.select_dtypes(include=int)

plt.figure(figsize=(28,10))
#i referencing subplot, j is refers to column names

for i,j in zip(range(1,10),int_cols):
  plt.subplot(3,3,i)
  plt.subplots_adjust(right=0.9,top=1.8)
  sns.boxplot(data = data,x = j)
  plt.title("Box of plot {}".format(j))

"""Description: Identify and visualize outliers of every Numerical column."""

float_cols = data.select_dtypes(include=float)

plt.figure(figsize=(28,10))
#i referencing subplot, j is refers to column names

for i,j in zip(range(1,10),float_cols):
  plt.subplot(3,3,i)
  plt.subplots_adjust(right=0.9,top=1.8)
  sns.boxplot(data = data,x = j)
  plt.title("Box of plot {}".format(j))

"""#Sleep Quality Analysis

Description: Explore the relationship between sleep duration and sleep quality.
"""

sns.scatterplot(x='Sleep Duration', y='Quality of Sleep', data=data)
plt.show()

"""Description: Explore the relationship between physical activity level and sleep quality."""

sns.boxplot(x='Physical Activity Level', y='Quality of Sleep', data=data)
plt.show()

"""Description: Explore the relationship between stress level and sleep quality."""

sns.boxplot(x='Stress Level', y='Quality of Sleep', data=data)
plt.show()

""" co-relationships between pairs of variables and identify potential correlations."""

corr=data.corr() #pearson corelation value
corr.style.background_gradient(cmap='coolwarm').set_precision(2)

corr = data.corr()
corr

