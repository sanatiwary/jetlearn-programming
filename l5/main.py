import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

plt.plot(x, y)
plt.show()

#ro, g^, r--, b--, b-
plt.plot(x, y, "b-")
plt.show()

plt.plot(x, y)
plt.axis([0, 10, 0, 200])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("sample graph")
plt.legend()
plt.show()

import numpy as np

x = np.arange(0, 10, 0.2)
print(x)

y1 = x**2
y2 = x**3

plt.plot(x, x**2, 'g--', x, x**3, 'b--')
plt.show()

x = np.arange(0, 18, 3)
m = 5
b = 4
y = m * x + b
plt.plot(x, y, 'r-')
plt.title("y = mx + b")
plt.show()

plt.bar([1, 3, 5, 7], [2, 4, 6, 8], color = 'b')
plt.bar([2, 4, 6, 8], [1, 3, 5, 7], color = 'r')
plt.show()

plt.bar(['male literacy','female literacy'], [90, 95])
plt.show()

plt.bar(['first class', 'business class', 'economy class'], [12, 30, 53])
plt.show()

xVals = []
yVals = []
for i in range(5):
    x = int(input("enter an x value for the equation: "))
    xVals.append(x)

print(xVals)

for i in range(5):
    y = xVals[i] * 4 + 10
    yVals.append(y)

plt.plot(xVals, yVals, 'g-')
plt.title("custom equation")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()