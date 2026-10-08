import numpy as np

# Create two matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# Print matrices and shapes
print("A:")
print(A)
print("Shape of A:", A.shape)

print("\nB:")
print(B)
print("Shape of B:", B.shape)


# Addition
print("\nAddition")
print("Shapes:", A.shape, B.shape)
print(A + B)


# Subtraction
print("\nSubtraction")
print("Shapes:", A.shape, B.shape)
print(A - B)


# Element-wise multiplication
print("\nElement-wise Multiplication")
print("Shapes:", A.shape, B.shape)
print(A * B)


# Matrix multiplication
print("\nMatrix Multiplication")
print("Shapes:", A.shape, B.shape)
print(A @ B)


# Transpose
print("\nTranspose of A")
print("Shape before:", A.shape)
print("Shape after:", A.T.shape)
print(A.T)


# Determinant
print("\nDeterminant of A")
print("Shape:", A.shape)
print(np.linalg.det(A))


# Inverse
print("\nInverse of A")
print("Shape:", A.shape)
print(np.linalg.inv(A))