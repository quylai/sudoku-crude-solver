import numpy as np





# a = np.arange(7)        # [0 1 2 3 4 5 6]
# b = np.arange(5)**2     # [ 0  1  4  9 16]


# for xdx, x in np.ndenumerate(a):
#   print("in a")
#   # print(type(x))


arr = np.arange(8)*3                    # [0  3  6  9 12 15 18 21]
evenFlags = np.array([0,0,0,0,0,0,0,0])

dummy = arr.copy()
for xdx, x in np.ndenumerate(dummy):
  if (x % 2 == 0):
    evenFlags[xdx] = 1
    arr[xdx] = 88

print(arr)
print(evenFlags)