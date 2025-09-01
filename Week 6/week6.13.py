n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
print("Enter elements of the first matrix:")
matrix1 = []
for i in range(n):
    row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
    matrix1.append(row)
print("Enter elements of the second matrix:")
matrix2 = []
for i in range(n):
    row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
    matrix2.append(row)
result = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)
print("Resultant matrix after addition:")
for row in result:
    print(" ".join(map(str, row)))
