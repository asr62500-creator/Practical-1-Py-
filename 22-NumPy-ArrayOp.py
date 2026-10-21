import numpy as np

# Create two NumPy arrays
A = np.array([10, 20, 30, 40])
B = np.array([1, 2, 3, 4])

print("Array A:", A)
print("Array B:", B)

# Element-wise arithmetic operations
print("Addition:", A + B)
print("Subtraction:", A - B)
print("Multiplication:", A * B)

# Statistical operations
print("Maximum of A:", np.max(A))
print("Minimum of A:", np.min(A))
print("Average of A:", np.mean(A))
print("Sum of A:", np.sum(A))