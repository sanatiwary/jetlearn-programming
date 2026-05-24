import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv("adult.csv", header=None)
data.columns = ["age", "workclass", "fnlwgt", "education", "educationNum", "maritalStatus", "occupation", "relationship", "race", "sex", "capitalGain", "capitalLoss", "hoursPerWeek", "nativeCountry", "income"]

print(data["age"].median(skipna=True))
data["age"].fillna(data["age"].median(skipna=True), inplace=True)

print(data["workclass"].value_counts().idxmax())
data["workclass"].fillna(data["workclass"].value_counts().idxmax(), inplace=True)

print(data["occupation"].value_counts().idxmax())
data["occupation"].fillna(data["occupation"].value_counts().idxmax(), inplace=True)

print(data["nativeCountry"].value_counts().idxmax())
data["nativeCountry"].fillna(data["nativeCountry"].value_counts().idxmax(), inplace=True)

data["workedAlone"] = np.where(data["relationship"] == "Unmarried", 1, 0)

from sklearn import preprocessing
labelEncoder = preprocessing.LabelEncoder()
data["workclass"] = labelEncoder.fit_transform(data["workclass"])
data["education"] = labelEncoder.fit_transform(data["education"])
data["maritalStatus"] = labelEncoder.fit_transform(data["maritalStatus"])
data["occupation"] = labelEncoder.fit_transform(data["occupation"])
data["relationship"] = labelEncoder.fit_transform(data["relationship"])
data["race"] = labelEncoder.fit_transform(data["race"])
data["sex"] = labelEncoder.fit_transform(data["sex"])
data["nativeCountry"] = labelEncoder.fit_transform(data["nativeCountry"])
data["income"] = labelEncoder.fit_transform(data["income"])

x = data[["age", "workclass", "fnlwgt", "education", "educationNum", "maritalStatus", "occupation", "relationship", "race", "sex", "capitalGain", "capitalLoss", "hoursPerWeek", "nativeCountry", "workedAlone"]]
y = data["income"]

from sklearn.model_selection import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=5)

from sklearn.tree import DecisionTreeClassifier
decisionTree = DecisionTreeClassifier()
decisionTree.fit(xTrain, yTrain)

yPred = decisionTree.predict(xTest)
from sklearn.metrics import accuracy_score, confusion_matrix
print(accuracy_score(yTest, yPred))

matrix = confusion_matrix(yTest, yPred)
sns.heatmap(matrix, annot=True, fmt="d")
plt.title("Decision Tree")
plt.xlabel("predicted")
plt.ylabel("actual")
plt.show()

from sklearn.ensemble import RandomForestClassifier
randomForest = RandomForestClassifier(n_estimators=100)
randomForest.fit(xTrain, yTrain)

yPred = randomForest.predict(xTest)
print(accuracy_score(yTest, yPred))

matrix = confusion_matrix(yTest, yPred)
sns.heatmap(matrix, annot=True, fmt="d")
plt.title("Random Forest")
plt.xlabel("predicted")
plt.ylabel("actual")
plt.show()
