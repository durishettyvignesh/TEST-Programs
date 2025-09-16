# Program to find the largest of three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("\nLargest number is:", a)
elif b >= a and b >= c:
    print("\nLargest number is:", b)
else:
    print("\nLargest number is:", c)

# using max function
print("\nLargest number is:", max(a, b, c))   