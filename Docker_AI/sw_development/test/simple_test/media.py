import pandas as pd

titanic = pd.read_csv("./data/titanic.csv")

print(titanic["Age"].mean())
print(titanic["PassengerId"].max())
print(titanic[titanic["PassengerId"]==titanic["PassengerId"].max() - 7])
print (titanic.info())
print(titanic.iloc[titanic.shape[0]-3:])
print(titanic.loc[:, ['Name', 'Sex']])
print(titanic.describe())