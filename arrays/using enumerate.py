import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
for i, x in enumerate(np.nditer(arr)):
    print(i, x)
