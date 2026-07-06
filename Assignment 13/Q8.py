import numpy as np

# Create a 4×4 matrix of random integers between 1 and 100
arr = np.random.randint(1, 101, (4, 4))

# Print the matrix
print("4×4 Random Integer Matrix:")
print(arr)

# Print array properties
print("\nShape:", arr.shape)
print("Dimension (ndim):", arr.ndim)
print("Total Number of Elements (size):", arr.size)
print("Data Type:", arr.dtype)
print("Minimum Value:", arr.min())
print("Maximum Value:", arr.max())