r, c = int(input('Enter row length: ')), int(input('Enter column length: '))
n = [[0 for i in range(c)] for j in range(r)]
print('Enter elements')
for i in range(r):
 for j in range(c):
   n[i][j] = int(input())
for i in range(r):
 s = 0
 for j in range(c):
   s += n[i][j]
 print(f'Sum of row {i + 1} = ', s)