import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in np.nditer(arr):
    print(x)


# Output:
# 1
# 2
# 3
# 4
# 5
# 6