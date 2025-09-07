import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
brr = np.array([[7, 8, 9], [10, 11, 12]])
crr = np.concatenate((arr, brr), axis=0)
print(crr)

#split array
drr = np.split(crr, 2, axis=0)
print(drr)

#live changes made
print("changes made")

#added extension
x = 5
print(x+8)
