import numpy as np

def linearEqn(a):
    x = np.arange(0, 11)
    y = (a * x)
    print(y)

def quadraticEqn(a, b):
    x = np.arange(0, 11)
    y = (a * x ** 2) + (b * x)
    print(y)

choice = input("enter 1 for linear or 2 for quadratic: ")

if choice == '1':
    a = int(input("enter the coefficient 'a': "))
    linearEqn(a)

elif choice == '2':
    a = int(input("Enter the coefficient 'a': "))
    b = int(input("Enter the coefficient 'b': "))
    quadraticEqn(a, b)

else:
    print("please enter one of the given options")
