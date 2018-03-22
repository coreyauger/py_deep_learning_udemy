import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('./data/titanic-train.csv')
print(type(df))
print(df.head())
print(df.info())
print(df.describe())

#Indexing
print(df.iloc[3])
print(df.loc[0:4,'Ticket'])
print(df['Ticket'].head())
print(df[['Embarked', 'Ticket']].head())

#Selections
print(df[df['Age'] > 70])
print(df['Age'] > 70)
print(df.query("Age > 70"))
print(df[(df['Age'] == 11) & (df['SibSp'] == 5)])
print(df[(df.Age == 11) | (df.SibSp == 5)])
print(df.query('(Age == 11) | (SibSp == 5)'))