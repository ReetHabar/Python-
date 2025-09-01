# Input dimensions for the first matrix
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))

# Initialize the first matrix
print("Enter elements of the first matrix row by row:")
matrix1 = []
for i in range(rows1):
    row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
    matrix1.append(row)

# Input dimensions for the second matrix
rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))

# Check if matrix multiplication is possible
if cols1 != rows2:
    print("Matrix multiplication is not possible with these dimensions.")
else:
    # Initialize the second matrix
    print("Enter elements of the second matrix row by row:")
    matrix2 = []
    for i in range(rows2):
        row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
        matrix2.append(row)

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    # Display the result
    print("Resultant matrix after multiplication:")
    for row in result:
        print(" ".join(map(str, row)))
