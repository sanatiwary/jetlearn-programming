def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        firstHalf = arr[:mid]
        lastHalf = arr[mid:]

        mergeSort(firstHalf)
        mergeSort(lastHalf)

        a = 0
        b = 0
        c = 0

        while a < len(firstHalf) and b < len(lastHalf):
            if firstHalf[a] < lastHalf[b]:
                arr[c] = firstHalf[a]
                a += 1
            else:
                arr[c] = lastHalf[b]
                b += 1
            c += 1

        while a < len(firstHalf):
            arr[c] = firstHalf[a]
            a += 1
            c += 1
        while b < len(lastHalf):
            arr[c] = lastHalf[b]
            b += 1
            c += 1

        return arr

arr = [7, 5, 13, 19, 2, 6, 8]
print(mergeSort(arr))