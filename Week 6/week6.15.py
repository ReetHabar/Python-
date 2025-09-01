rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
print("Enter the elements of the matrix row by row:")
for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
    matrix.append(row)
flattened_matrix = [element for row in matrix for element in row]
flattened_matrix.sort()
sorted_matrix = []
for i in range(rows):
    row = flattened_matrix[i * cols:(i + 1) * cols]
    sorted_matrix.append(row)
print("Sorted matrix:")
for row in sorted_matrix:
    print(" ".join(map(str, row)))
