def gcf(a, b):
    gcf = 1
    if ((a - b) > 0):
        small = b
    else:
        small = a

    for i in range(small, 1, -1):
        if(a % i == 0 and b % i == 0):
            gcf = i
            break
    
    return str(gcf)

a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
print("the gcf of {} and {} is ".format(a, b) + gcf(a, b))