# Loading the Dataset:
import pandas as pd
import numpy as np
data = pd.read_csv('data.csv')
# First 5
print(data.head())

#Information columns and raws
print(data.info())

print(data.describe())

#  Row and column selection is made on the DataFrame using the loc index. The loc index is used to select rows and columns as row representations or boolean-based metrics.

# Data
data = pd.DataFrame({
    'Name': ['Harry', 'Hermonie', 'Draco', 'Ron', 'Severus'],
    'Age': [15, 14, 16, 15, 50]
})

# 'Harry' satırını seçme
selected_row = data.loc[data['Name'] == 'Harry']
print(selected_row)

# 'Alice' satırının 'Age' sütununu seçme
selected_value = data.loc[data['Name'] == 'Harry', 'Age']
print(selected_value)
# İkinci ve üçüncü satırları seçme
selected_rows = data.loc[1:2]
print(selected_rows)

# Yaşı 45'den büyük olan satırları seçme
selected_rows = data.loc[data['Age'] > 45]
print(selected_rows)

#GROUP BY

# Data
data = pd.DataFrame({
    'Name': ['Gandalf', 'Aragorn', 'Galadriel', 'Legolas', 'Arwen'],
    'Department': ['HR', 'IT', 'HR', 'IT', 'HR'],
    'Salary': [6000, 8000, 7500, 7000, 5500]
})
# Departman
grouped = data.groupby('Department')

# Her departman için ortalama maaşı hesaplama
average_salary = grouped['Salary'].mean()
print("Ortalama Maaşlar:")
print(average_salary)

# Her departmandaki en yüksek ve en düşük maaşları bulmak için
salary_summary = grouped['Salary'].agg(['max', 'min'])
print("\nMaaş Özetlemesi:")
print(salary_summary)

#JOIN & MERGE

# Öğrenci veri kümesi
student_data = pd.DataFrame({
    'StudentID': [1, 2, 3],
    'Name': ['Hagrid', 'Snape', 'McGonagall'],
    'Age': [45, 50, 60]
})

# Notlar veri kümesi
grades_data = pd.DataFrame({
    'StudentID': [1, 2, 3],
    'Course': ['Sihirli Yaratıkların Bakımı / Bekçi', 'Karanlık Sanatlara Karşı Savunma', 'Şekil Değiştirme'],
    'Grade': ['A', 'B', 'A']
})

# Inner Join: İki veri kümesindeki eşleşen satırları birleştirir.
inner_merged = student_data.merge(grades_data, on='StudentID', how='inner')
print("Inner Join:")
print(inner_merged)

# Left Join: Sol veri kümesindeki tüm satırları ve sağ veri kümesindeki eşleşen satırları birleştirir.
left_merged = student_data.merge(grades_data, on='StudentID', how='left')
print("\nLeft Join:")
print(left_merged)

# Right Join: Sağ veri kümesindeki tüm satırları ve sol veri kümesindeki eşleşen satırları birleştirir.
right_merged = student_data.merge(grades_data, on='StudentID', how='right')
print("\nRight Join:")
print(right_merged)

# Outer Join: İki veri kümesindeki tüm satırları birleştirir, eşleşen satırları eşleşmeyenlerle birleştirir.
outer_merged = student_data.merge(grades_data, on='StudentID', how='outer')
print("\nOuter Join:")
print(outer_merged)