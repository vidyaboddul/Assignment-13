import numpy as np

# Create two 3×3 matrices
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

# Matrix addition
addition = A + B

# Matrix multiplication
matrix_multiplication = A @ B
# (You can also use: np.dot(A, B))

# Element-wise multiplication
elementwise_multiplication = A * B

# Print the results
print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMatrix Addition (A + B):")
print(addition)

print("\nMatrix Multiplication (A @ B):")
print(matrix_multiplication)

print("\nElement-wise Multiplication (A * B):")
print(elementwise_multiplication)