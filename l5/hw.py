import matplotlib.pyplot as plt
import numpy as np

def linear():
    m = int(input("m:"))
    b = int(input("b:"))
    x = np.arange(0, 50, 1)
    y = m * x + b
    plt.plot(x, y, 'g-')
    plt.title("linear equation")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.show()

def quadratic():
    a = int(input("x^2 coefficient: "))
    b = int(input("x coefficient: "))
    c = int(input("constant: "))
    x = np.arange(0, 50, 1)
    y = a * x**2 + b * x + c
    plt.plot(x, y, 'r-')
    plt.title("quadratic equation")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.show()

def cubic():
    a = int(input("x^3 coefficient: "))
    b = int(input("x^2 coefficient: "))
    c = int(input("x coefficient: "))
    d = int(input("constant: "))
    x = np.arange(0, 50, 1)
    y = a * x**3 + b * x**2 + c * x + d
    plt.plot(x, y, 'b-')
    plt.title("cubic equation")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.show()

choice = int(input("choose 1 for linear, 2 for quadratic, or 3 for cubic: "))

if choice == 1:
    linear()
elif choice == 2:
    quadratic()
elif choice == 3:
    cubic()
else:
    print("pick 1, 2, or 3")
