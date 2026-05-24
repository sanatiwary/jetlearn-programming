import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("adult.csv")

data.columns = ("age", "work_class", "registration", "education", "grade_level", "marital_status", "occupation", "relationship", "race", "gender", "capGain", "capLoss", "hours_per_week", "country", "income")

data.rename(
    columns={
        "work_class" : "workClass",
        "grade_level" : "gradeLevel",
        "marital_status" : "maritalStatus",
        "hours_per_week" : "hoursPerWeek"
    }, inplace=True
)

# shows numerical data of the columns
print(data.describe())

print(data.info())

print(data.isnull().sum())

print(data.isin(['?']).sum())

for i in data.columns:
    print(data[i].value_counts())

data.drop(["age", "workClass", "registration", "capGain", "capLoss"], axis=1, inplace=True)

print(data.head())

income = set(data["income"])
print(income)

data["income"] = data["income"].map({" <=50K" : 0, " >50K" : 1}).astype(int)
print(data.head())

data["gender"] = data["gender"].map({" Male" : 0, " Female" : 1}).astype(int)
print(data.head())

race = set(data["race"])
print(race)

data["race"] = data["race"].map(
    {" Other" : 0, 
     " Asian-Pac-Islander" : 1,
     " White" : 2, 
     " Amer-Indian-Eskimo" : 3,
     " Black" : 4}
    ).astype(int)
print(data.head(100))

data.groupby("gender").income.mean().plot(kind="bar")
plt.show()

data.groupby("race").income.mean().plot(kind="bar")
plt.show()