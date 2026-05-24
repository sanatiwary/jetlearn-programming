import pandas as pd

data = pd.read_csv("titanic.csv")

meanAgeSexPclass = data.groupby(["Sex", "Pclass"])["Age"].mean()
print(meanAgeSexPclass)

died = data.loc[data["Survived"] == 0]
medianAgeDiedSex = died.groupby("Sex")["Age"].median()
meanAgeDiedSex = died.groupby("Sex")["Age"].mean()

print(medianAgeDiedSex)
print(meanAgeDiedSex)