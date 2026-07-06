import numpy as np

# a) 1D array of 10 random numbers between 0 and 1
arr1 = np.random.rand(10)

# b) 3×3 matrix of random numbers from standard normal distribution
arr2 = np.random.randn(3, 3)

# c) 2D array (4×5) of random integers between 10 and 50
arr3 = np.random.randint(10, 51, (4, 5))

# Print the arrays
print("a) 1D Array of 10 Random Numbers (0 to 1):")
print(arr1)

print("\nb) 3×3 Matrix of Random Numbers (Standard Normal Distribution):")
print(arr2)

print("\nc) 4×5 Array of Random Integers (10 to 50):")
print(arr3)