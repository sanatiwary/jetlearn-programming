import numpy as np
sample = [1, 2, 3, 4]
print(type(sample))

sampleNumpy = np.array(sample)
print(type(sampleNumpy))

# errorArray = np.array([1, 2, 4], "name")

a = np.array([1, 2, 3])
a += 10
print(a)

a0 = np.zeros(10)
print(a0)

a1 = np.ones(10)
print(a1)

fArray = np.array([1, 2, 3, 4, 5], dtype = "f")
print(fArray)

array2d = np.array([[1, 2], [3, 4]])
print(array2d)

print("array dimension: ", array2d.ndim)
print("numbers of rows/col: ", array2d.shape)
print("number of elements: ", array2d.size)
print("array byte size: ", array2d.nbytes)

numArray = np.arange(1, 100)
print(numArray)

evenArray = np.arange(2, 100, 2)
print(evenArray)

randArray = np.random.permutation(np.arange(1, 11))
print(randArray)

randNum = np.random.randint(1, 10)
print(randNum)

randArray2 = np.random.rand(2, 3)
print(randArray2)
print(randArray2.shape)

reshapedArray = np.arange(1, 10).reshape(3, 3)
print(reshapedArray)
print(reshapedArray)

numArray2 = np.arange(1, 37)
print(numArray2)

reshapedArray2 = numArray2.reshape(6, 6)
print(reshapedArray2)

reshapedArray3 = numArray2.reshape(12, 3)
print(reshapedArray3)

reshapedArray4 = numArray2.reshape(3, 12)
print(reshapedArray4)

reshapedArray5 = numArray2.reshape(36, 1)
print(reshapedArray5)

reshapedArray6 = numArray2.reshape(2, 18)
print(reshapedArray6)

reshapedArray7 = numArray2.reshape(18, 2)
print(reshapedArray7)

reshapedArray8 = numArray2.reshape(9, 4)
print(reshapedArray8)

reshapedArray9 = numArray2.reshape(4, 9)
print(reshapedArray9)

randArray2 = np.random.permutation(np.arange(1, 21))
print(randArray2)

sortedArray = np.sort(randArray2)
print(sortedArray)