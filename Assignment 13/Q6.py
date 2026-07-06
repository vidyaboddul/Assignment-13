import numpy as np

# Create two vectors
v1 = np.array([2, 4, 6, 8])
v2 = np.array([1, 3, 5, 7])

# Perform operations
addition = v1 + v2
subtraction = v1 - v2
multiplication = v1 * v2
dot_product = np.dot(v1, v2)

# Print the results
print("Vector 1:")
print(v1)

print("\nVector 2:")
print(v2)

print("\nAddition:")
print(addition)

print("\nSubtraction:")
print(subtraction)

print("\nElement-wise Multiplication:")
print(multiplication)

print("\nDot Product:")
print(dot_product)