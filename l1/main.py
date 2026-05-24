x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

# m = sum((xi-mean(x)) * (yi-mean(y))) / sum((xi – mean(x))^2)
# c = mean(y) – m * mean(x)

def findMean(a):
    return sum(a)/len(a)

meanX = findMean(x)
meanY = findMean(y)

num = 0
den = 0

for i in range(len(x)):
    num += ((x[i] - meanX) * (y[i] - meanY))
    den += pow((x[i] - meanX), 2)

m = num / den
print("m = ", m)

c = round(meanY - m * meanX, 1)
print("c = ", c)

from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([[1], [2], [3], [4], [5]])

reg = LinearRegression().fit(X, y)

print("m = ", reg.coef_)
print("c = ", reg.intercept_)

x1 = np.array([[2], [4], [6], [8], [10]])
y1 = np.array([[1], [3], [5], [7], [9]])

reg1 = LinearRegression().fit(x1, y1)

print("m = ", reg1.coef_)
print("c = ", reg1.intercept_)