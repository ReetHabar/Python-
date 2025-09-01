m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))
matrix = []

print("Enter the elements row by row:")
for i in range(m):
    row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
    matrix.append(row)

for i in range(m):
    row_sum = sum(matrix[i])
    print(f"Sum of row {i+1} = {row_sum}")
