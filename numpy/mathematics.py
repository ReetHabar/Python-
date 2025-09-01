import numpy as np

# Create two sample arrays
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Element-wise operations
sum_AB = A + B
diff_AB = A - B
prod_AB = A * B  # Element-wise multiplication
div_AB = A / B   # Element-wise division

print("\nElement-wise Addition:\n", sum_AB)
print("Element-wise Subtraction:\n", diff_AB)
print("Element-wise Multiplication:\n", prod_AB)
print("Element-wise Division:\n", div_AB)

# Matrix multiplication (dot product)
dot_product = np.dot(A, B)

print("\nDot Product (Matrix Multiplication):\n", dot_product)

# Transpose of a matrix
transpose_A = np.transpose(A)
print("\nTranspose of A:\n", transpose_A)

# Finding the determinant of a matrix
det_A = np.linalg.det(A)
print("\nDeterminant of A:", det_A)

# Computing the inverse of a matrix (if it is invertible)
try:
    inverse_A = np.linalg.inv(A)
    print("\nInverse of A:\n", inverse_A)
except np.linalg.LinAlgError:
    print("\nMatrix A is not invertible.")

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\nEigenvalues of A:\n", eigenvalues)
print("\nEigenvectors of A:\n", eigenvectors)

# Statistical operations
mean_A = np.mean(A)
median_A = np.median(A)
std_A = np.std(A)

print("\nMean of A:", mean_A)
print("Median of A:", median_A)
print("Standard Deviation of A:", std_A)

# Summation and cumulative sum
sum_elements_A = np.sum(A)
cumsum_A = np.cumsum(A)

print("\nSum of all elements in A:", sum_elements_A)
print("Cumulative Sum of A:\n", cumsum_A)

# Element-wise exponential and logarithm
exp_A = np.exp(A)
log_A = np.log(A)

print("\nExponential of A:\n", exp_A)
print("Natural Logarithm of A:\n", log_A)
