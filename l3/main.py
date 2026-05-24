def fib(n):
    if (n == 0):
        return 0
    if(n == 1 or n == 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
n = int(input("enter a number: "))
print("fibonacci series of {} is: ".format(n), end = " ")

for i in range(0, n):
    print(fib(i), end = " ")