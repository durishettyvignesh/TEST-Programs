arr = [10, 20, 30, 40, 30, 50]

print(arr)
arr = [x for x in arr if x != 30]
print(arr)   # [10, 20, 40, 50]


