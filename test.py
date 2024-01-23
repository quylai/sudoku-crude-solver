import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

i = 1
# Access the ith column (0-indexed)
ith_column = arr[:, i]

print(ith_column)