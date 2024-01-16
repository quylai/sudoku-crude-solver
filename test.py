import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 8])
iVal = [2, 4, 6]

print(arr)

x = np.where(arr == iVal[0])

print("x is" + str(x))
print(x[0])