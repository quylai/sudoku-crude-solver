import numpy as np





# a = np.arange(7)        # [0 1 2 3 4 5 6]
# b = np.arange(5)**2     # [ 0  1  4  9 16]

arr = np.array([[0,3,0,3], [0,3,3,6], [0,3,6,9],
                [3,6,0,3], [3,6,3,6], [3,6,6,9],
                [6,9,0,3], [6,9,3,6], [6,9,6,9]])




dummy = arr.copy()
for xdx, x in np.ndenumerate(dummy.flat):
  print("xdx is " + str(xdx))


