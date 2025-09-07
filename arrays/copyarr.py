import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
# Output:
# [42  2  3  4  5]
# [1  2  3  4  5]
#added extension
x = 5
print(x)
