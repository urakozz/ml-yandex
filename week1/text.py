import pandas
import seaborn as sns
import numpy as np

sns.set(color_codes=True)
data = pandas.read_csv('titanic.csv', index_col='PassengerId')

print("\n1 Men/Women:")
print(data["Sex"].value_counts())

x = np.random.normal(size=100)
sns.distplot(x)

print("\n2 Survived")
print(data["Survived"].value_counts(normalize=True))

print("\n3 classes")
print(data["Pclass"].value_counts(normalize=True))

print("\n4 age mean/median")
print(data["Age"].mean())
print(data["Age"].median())

print("\n5 correlation")
print(data["Parch"].corr(data["SibSp"], method='pearson'))

print("\n6 women name")
print("\n6 women name")
print(data[data["Sex"]=="female"]["Name"].str.split(pat=", ", expand=True)[1].str.split(pat=" ").str[1].value_counts().head())
