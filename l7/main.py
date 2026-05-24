import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')
print(dataset.info())

#features (input) - country, age, salary
#target (output) - purchased?

X = dataset.iloc[:, :-1].values # all except last
y = dataset.iloc[:, -1].values # pick last column

print("features: \n", X)
print("targets: \n", y)
print()

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")

# applying imputer to age and salary -- replacing nan with mean values
X[:, 1:3] = imputer.fit_transform(X[:, 1:3])

print("after imputing: \n", X)
print()

# encoding categorical data to numerical values (replacing country names with 0, 1, 2)
# encoding the independent variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [0])], remainder="passthrough")
X = pd.DataFrame(ct.fit_transform(X))
print("one hot encoding: \n", X)
print()

# encoding the dependent variable - target has to be 1d (true/false) so shouldnt use encoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print('label encoder: \n', y)
print()

# splitting the dataset into training and testing
from sklearn.model_selection import train_test_split
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=1)
print("Xtrain: \n", XTrain)
print("Xtest: \n", XTest)
print()
print("ytrain: \n", yTrain)
print("ytest: \n", yTest)

# feature scaling - age and salary (scaling so system not affected by huge varation in values)
# StandardScaler = (x-mean)/stdev (values will be -1 to 1, mean 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

XTrain.iloc[:, 1:3] = sc.fit_transform(XTrain.iloc[:, 1:3])
XTest.iloc[:, 1:3] = sc.fit_transform(XTest.iloc[:, 1:3])

print("after scaling the values from -1 to 1: \n ")
print(XTrain)
print(XTest)