import csv

def findMean(a):
    return sum(a) / len(a)

x = []
y = []

with open('titanic.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[4] and row[7]:
            x.append(float(row[4]))
            y.append(float(row[7]))

meanX = findMean(x)
meanY = findMean(y)

num = 0
den = 0

for i in range(len(x)):
    num += ((x[i] - meanX) * (y[i] - meanY))
    den += pow((x[i] - meanX), 2)

m = num / den
print("m = ", m)

c = round(meanY - m * meanX, 1)
print("c = ", c)
