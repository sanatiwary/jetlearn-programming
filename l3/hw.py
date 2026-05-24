import pandas as pd

df = pd.read_csv('iris.csv')

print(df.head())
print(df.info())

print(df['petal_length'].mean())
print(df['petal_length'].min())
print(df['petal_length'].max())

print(df['petal_width'].mean())
print(df['petal_width'].min())
print(df['petal_width'].max())

print(df['sepal_length'].mean())
print(df['sepal_length'].min())
print(df['sepal_length'].max())

print(df['sepal_width'].mean())
print(df['sepal_width'].min())
print(df['sepal_width'].max())

print(df['species'].value_counts())
