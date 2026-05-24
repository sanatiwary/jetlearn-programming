import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(a[0])
print(a[0:4])
print(a[:4]) # from start
print(a[5:]) # til end
print(a[0:8:2]) # start : end : step
print(a[::2]) # from start til end, every 2nd value
print(a[::-1]) # reverse array

multiArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(multiArray[0:2, 0:2])

array7by7 = np.arange(1, 50).reshape(7, 7)
print(array7by7)
print(array7by7[2:5, 2:5])

k = np.array([1, 2, 3, 4, 5, 6, 7, 8])
evenArray = k[k % 2 == 0]
print("even array: ", evenArray)

oddArray = k[k % 2 != 0]
print("odd array: ", oddArray)

b = k[k == 5]
print(b)

b = k[k == 500]
print(b)

print(k[[2, 4, 6]]) # all indexes

c = np.arange(1, 10)
print(c[c < 5])

sampleList = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(0, len(sampleList)):
    sampleList[i] += 1
print(sampleList)

sampleArray = np.arange(1, 9)
sampleArray += 1
print(sampleArray)

sampleArray1 = np.arange(1, 9)
sampleArray2 = np.arange(1, 9)
result = sampleArray1 + sampleArray2
print("sum of array: ", result)

result = sampleArray1 - sampleArray2
print("difference of array", result)


matA = np.random.permutation(np.arange(16).reshape(4, 4))
print("matA: \n", matA)

matB = np.random.permutation(np.arange(16).reshape(4, 4))
print("matB: \n", matB)

print("sum of matA and matB: \n", matA + matB)

def linearEqn(x):
    y = (2*x) + 3
    print(y)

linearEqn(10)
l = np.arange(1, 6)
linearEqn(l)