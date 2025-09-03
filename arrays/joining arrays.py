import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
brr = np.array([[7, 8, 9], [10, 11, 12]])
crr = np.concatenate((arr, brr), axis=0)
print(crr)

