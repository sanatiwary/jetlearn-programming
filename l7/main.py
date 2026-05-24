import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv("student-mat.csv")
print(data.head())
# used to check for any null values in columns
print(data.info())
# describe takes numerical data and provides that
print(data.describe())

from sklearn import preprocessing
labelEncoder = preprocessing.LabelEncoder()

data["school"] = labelEncoder.fit_transform(data["school"])
data["sex"] = labelEncoder.fit_transform(data["sex"])
data["famsize"] = labelEncoder.fit_transform(data["famsize"])
data["Pstatus"] = labelEncoder.fit_transform(data["Pstatus"])
data["Mjob"] = labelEncoder.fit_transform(data["Mjob"])
data["reason"] = labelEncoder.fit_transform(data["reason"])
data["guardian"] = labelEncoder.fit_transform(data["guardian"])
data["schoolsup"] = labelEncoder.fit_transform(data["schoolsup"])
data["famsup"] = labelEncoder.fit_transform(data["famsup"])
data["paid"] = labelEncoder.fit_transform(data["paid"])
data["activities"] = labelEncoder.fit_transform(data["activities"])
data["nursery"] = labelEncoder.fit_transform(data["nursery"])
data["higher"] = labelEncoder.fit_transform(data["higher"])
data["internet"] = labelEncoder.fit_transform(data["internet"])
data["romantic"] = labelEncoder.fit_transform(data["romantic"])

data.drop("G1", axis=1, inplace=True)
data.drop("G2", axis=1, inplace=True)

# data analysis - segregating input and outputs
x = data[["school", "sex", "age", "famsize", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "reason", "guardian", "traveltime", "studytime", "failures", "schoolsup", "famsup", "paid", "activities", "nursery", "higher", "internet", "romantic", "famrel", "freetime", "goout", "Dalc", "Walc", "health", "absences"]]
y = data["G3"]

from sklearn.model_selection import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=5)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=100)
classifier.fit(xTrain, yTrain)

yPred = classifier.predict(xTest)
print(yPred)

from sklearn.metrics import confusion_matrix
matrix = confusion_matrix(yTest, yPred)
sns.heatmap(matrix, annot=True, fmt="d")
plt.title("matrix")
plt.xlabel("predicted")
plt.ylabel("actual")
plt.show()