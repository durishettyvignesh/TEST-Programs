#reshape new arr

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
arr = arr.reshape((2, 3))
print(arr)

for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        print(arr[i, j])
# Output:
# 1
# 2
# 3
# 4
# 5
# 6