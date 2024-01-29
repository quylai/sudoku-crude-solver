import numpy as np


charary = np.chararray((4, 5))
print(charary)
print("----")

charary = np.chararray(charary.shape, itemsize=7)
print(charary)

