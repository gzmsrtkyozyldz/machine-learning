import pandas as pd

data = pd.DataFrame({
    'StudentID': [1, 2, 3, 4, 5],
    'Name': ['McGonagall', 'Lupin', 'Dumbledore', 'Moody', 'Umbridge'],
    'Age': [60, 45, 78, 50, 55],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female']
})

# Control
print(data.isnull().sum())

# Veri temizleme: Yaşı 50den küçük olan kayıtları çıkartma
data = data[data['Age'] >= 50]

# KOne-Hot Encoding
data = pd.get_dummies(data, columns=['Gender'], drop_first=True)


def categorize_age(age):
    if age < 54:
        return 'Young'
    elif age < 60:
        return 'Middle'
    else:
        return 'Old'


data['AgeCategory'] = data['Age'].apply(categorize_age)

