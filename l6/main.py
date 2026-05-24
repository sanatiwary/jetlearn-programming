import matplotlib.pyplot as plt

ages = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins, histtype='bar', rwidth=0.8)
plt.xlabel("age interval")
plt.ylabel("frequency")
plt.title("histogram")
plt.show()

grades = [63, 75, 82, 78, 94, 99, 92, 89]
bins = [60, 65, 70, 75, 80, 85, 90, 95, 100]

plt.hist(grades, bins, histtype='bar', rwidth=0.8)
plt.xlabel("grades")
plt.ylabel("frequency")
plt.title("histogram 2")
plt.show()

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [0, 1, 0, 1, 0, 1, 0, 1, 0]

plt.scatter(x, y, label="scatter plot", color="red", marker='o', s=50)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("scatter plot")
plt.legend()
plt.show()

x = [10, 12, 5, 7, 8, 12, 4, 9]
y = [0, 1, 3, 1, 0, 6, 1, 3]

plt.scatter(x, y, label="scatter plot 2", color="blue", marker='o', s=50)
plt.xlabel('x')
plt.ylabel('y')
plt.title("scatter plot 2")
plt.legend()
plt.show()

activites = ["sleeping", "eating", "working", "netflix", "workout", "friends"]
slices = [6, 13, 2, 9, 5, 10]

clr = ['c', 'm', 'r', 'b', 'g', 'y']

plt.pie(slices, labels=activites, colors=clr, startangle=90, shadow=True)
plt.title("day chart")
plt.show()

subjects = ["english", "math", "history", "science", "arts", "gym"]
slices = [5, 7, 4, 5, 9, 9]

clr = ['r', 'b', 'y', 'g', 'm', 'c']

plt.pie(slices, labels=subjects, colors=clr, startangle=90, shadow=True)
plt.title("favorite subjects")
plt.show()

days = [1, 2, 3, 4, 5]

eating = [2, 3, 4, 3, 2]
sleeping = [7, 8, 6, 11, 7]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

plt.plot([], [], color='m', label="eating", linewidth=5)
plt.plot([], [], color='c', label="sleeping", linewidth=5)
plt.plot([], [], color='r', label="working", linewidth=5)
plt.plot([], [], color='k', label="playing", linewidth=5)

plt.stackplot(days, eating, sleeping, working, playing, colors = ['m', 'c', 'r', 'k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title("stack plot")
plt.legend()
plt.show()

import numpy as np

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0, 5, 0.1)
t2 = np.arange(0, 5, 0.2)

plt.figure()

plt.subplot(221)
plt.plot(t1, f(t1), 'bo')

plt.subplot(224)
plt.plot(t2, np.cos(2*np.pi*t2))

plt.show()

