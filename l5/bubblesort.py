ogList = [12, 35, 2, 8, 53, 6, 9]

for i in range(len(ogList)):
    for a in range(i, len(ogList)):
        if ogList[i] > ogList[a]:
            ogList[i], ogList[a] = ogList[a], ogList[i]

print(ogList)