n = int(input("Enter the size of the magic square (odd number): "))

magic_square = [[0] * n for _ in range(n)]

row, col = 0, n // 2

for num in range(1, n * n + 1):
    magic_square[row][col] = num
    new_row = (row - 1) % n
    new_col = (col + 1) % n
    if magic_square[new_row][new_col]: 
        row += 1
    else:
        row, col = new_row, new_col

print("Magic Square:")
for row in magic_square:
    print(" ".join(str(x) for x in row))
