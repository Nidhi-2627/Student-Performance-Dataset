
# Import libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""# **1. Load Dataset**"""

df =pd.read_csv('/content/student-mat.csv', sep=';')
df.head()

"""# **2. Explore & Clean Data**"""

#Missing values
df.isnull().sum()

# check the shape(Rows,columns)
print(f"Dataset shape : {df.shape}")

# Remove Duplication
df =df.drop_duplicates()

#check Data tyoes
df.dtypes

"""# **3. Data Analysis**"""

#1 Average final grade(G3)

avg_grade =df['G3'].mean()
print("Average Final Grade:",avg_grade)

#Student score above 15
above_15 =df[df['G3']>15].shape[0]
print("students scoring above 15:",above_15)

#correlation(student time vs performance)

correlation =df['studytime'].corr(df['G3'])
print("correlation between study time and G3:",correlation)

# Gender performance comparison
gender_avg = df.groupby('sex')['G3'].mean()
print(gender_avg)

"""# 4. Visualizations"""

# 1. Histogram of Grades

plt.figure(figsize=(8,5))
plt.hist(df['G3'], bins=10)
plt.title("Distribution of Final Grades")
plt.xlabel("Grades")
plt.ylabel("Frequency")
plt.show()

# 2. Scatter Plot (Study Time vs Grades)
plt.figure(figsize=(8,5))
plt.scatter(df['studytime'], df['G3'])
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("Final Grade")
plt.show()

#3. Bar Chart (Gender vs Average Score)
gender_avg.plot(kind='bar')
plt.title("Average Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Grade")
plt.show()

#Bonus (Optional Section)
## ⭐ Bonus
sns.histplot(df['G3'], kde=True)
plt.show()
