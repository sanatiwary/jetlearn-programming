import pandas as pd

data = pd.read_csv("titanic.csv")

adultNames = data.loc[data["Age"] > 18, "Name"]
print(adultNames)

print(data.iloc[9:25, 2:5])

data.iloc[0:3, 2] = "sana"
print(data.iloc[0:3, 2])

data.to_csv("sana.csv")

data["Test"] = data["Fare"] + 2
data["Test2"] = data["Fare"] * data["Pclass"]
print(data.head())

dataRenamed = data.rename(
    columns = {
        "Pclass" : "Passenger Class"
    }
)

print(dataRenamed.info())

print(data["Age"].mean())
print(data[["Age", "Fare"]].mean)

print(data.agg({
    "Age" : ["min", "max", "median"],
    "Fare" : ["min", "max"]
}))

print(data[["Sex", "Age"]].groupby("Sex").mean())
print(data.groupby("Sex")["Age"].mean())

print(data.groupby(["Sex", "Pclass"])["Fare"].mean())

print(data["Pclass"].value_counts())

a = data.sort_values(by = "Age")
print(a[["Name", "Age"]])

b = data.sort_values(by = "Age", ascending=False)
print(b[["Name", "Age"]])

data["nameLowerCase"] = data["Name"].str.lower()
print(data.head())

data["sexShort"] = data["Sex"].replace({"male" : "m", "female" : "f"})
print(data.head())