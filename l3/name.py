import pandas as pd

df = pd.DataFrame({
    "name" : ["sana", "sindhuja", "a", "b", "c", "d", "e"],
    "age" : [15, 26, 1, 2, 3, 4, 5],
    "city" : ["fremont", "madurai", "x", "y", "z", "q", "r"]
})

print(df)
print(df.head(3))

print("rows and cols", df.shape)

print(df["name"])
print(df["age"].max())
print(type(df["age"]))
print(df["age"].shape)
print(df.info())
print(df.describe())

data = pd.read_csv("titanic.csv")
print(data.head())
print(data.info())

nameAndAge = data[["Name", "Age"]]
print(nameAndAge.head())
print(nameAndAge.shape)

above35 = data[data["Age"] > 35]
print(above35.head())
print(above35.shape)

class2and3 = data[data["Pclass"].isin([2, 3])]
print(class2and3[["Name", "Pclass"]].head())

class2and3 = data[(data["Pclass"] == 2) | (data["Pclass"] == 3)]
print(class2and3[["Name", "Pclass"]].head())

fare = data[(data["Pclass"] == 1) & (data["Sex"] == "male")]
print(fare["Fare"].mean())
