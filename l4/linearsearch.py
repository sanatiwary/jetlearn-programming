arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = int(input("enter the value you want to look for: "))

for i in range(0, len(arr)):
    if arr[i] == key:
        print("key is found!")
        break
    
if key in arr:
    print("key is found!")

for num in arr:
    if num == key:
        print("key is found!")