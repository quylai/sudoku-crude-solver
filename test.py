import numpy as np



# a = np.arange(7)        # [0 1 2 3 4 5 6]
# b = np.arange(5)**2     # [ 0  1  4  9 16]
c = np.array([0,0,0,8,0,0,0,0,0,0])
d = np.array([0,0,0,0,0,0,0,0,0,0])

# arr = np.array([[0,3,0,3], [0,3,3,6], [0,3,6,9],
#                 [3,6,0,3], [3,6,3,6], [3,6,6,9],
#                 [6,9,0,3], [6,9,3,6], [6,9,6,9]])


print(np.nonzero(c))            # (array([3], dtype=int64),)
print(np.nonzero(c)[0])         # [3]
print(np.nonzero(c)[0][0])      # 3

print()
