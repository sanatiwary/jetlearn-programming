arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = int(input("enter the value you want to look for: "))

min = arr[0]
max = len(arr) - 1

found = False

while min <= max:
    mid = (min + max) // 2

    if arr[mid] == key:
        print("key is found")
        found = True
        break
    elif arr[mid] < key:
        min = mid + 1
    else:
        max = mid - 1

if found == False:
    print("no key found")