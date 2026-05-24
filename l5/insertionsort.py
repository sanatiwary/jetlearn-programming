ogList = [12, 35, 2, 8, 53, 6, 9]

for i in range(1, len(ogList)):
    temp = ogList[i]
    j = i - 1
    while j >= 0 and temp < ogList[j]:
        ogList[j + 1] = ogList[j]
        j -= 1
    ogList[j + 1] = temp

print(ogList)