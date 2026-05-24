import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("car.csv")
data.columns = ("sales", "maintenence", "doors", "persons", "boot_space", "safety", "class")

print(data.head())
print(data.describe())
print(data.info())

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

data["sales"] = le.fit_transform(data["sales"])
data["maintenence"] = le.fit_transform(data["maintenence"])
data["doors"] = le.fit_transform(data["doors"])
data["persons"] = le.fit_transform(data["persons"])
data["boot_space"] = le.fit_transform(data["boot_space"])
data["safety"] = le.fit_transform(data["safety"])
data["class"] = le.fit_transform(data["class"])

x = data[["sales", "maintenence", "doors", "persons", "boot_space", "safety"]]
y = data["class"]

from sklearn.model_selection import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=2)

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion="entropy", random_state=0)

classifier.fit(xTrain, yTrain)
yPred = classifier.predict(xTest)

from sklearn.metrics import classification_report, confusion_matrix
matrix = confusion_matrix(yTest, yPred)

sns.heatmap(matrix, annot=True, fmt="d")
plt.title("matrix")
plt.xlabel("predicted")
plt.ylabel("actual")
plt.show()