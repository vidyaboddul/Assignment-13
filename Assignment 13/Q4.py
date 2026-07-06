import numpy as np

# a) 10 equally spaced numbers between 0 and 5
arr1 = np.linspace(0, 5, 10)

# b) 15 equally spaced numbers between 10 and 100
arr2 = np.linspace(10, 100, 15)

# Print the arrays and their lengths
print("a) 10 equally spaced numbers between 0 and 5:")
print(arr1)
print("Length:", len(arr1))

print("\nb) 15 equally spaced numbers between 10 and 100:")
print(arr2)
print("Length:", len(arr2))