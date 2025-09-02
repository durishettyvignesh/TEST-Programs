import numpy as sp
arr = sp.array([[[1,2,3] , [4,5,6]] , [[7,8,9] , [10,11,12]]])
print(arr)
print(arr.ndim)
print(arr.shape)

# Print the total number of elements in the array
print(arr.size)

#this prints all the array index with the elements
for index, value in sp.ndenumerate(arr):
    print("Index:", index, "Value:", value)
