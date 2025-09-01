r, c = int(input('Enter row length: ')), int(input('Enter column length: '))
n = [[0 for i in range(c)] for j in range(r)]
print('Enter matrix 1 elements')
for i in range(r):
 for j in range(c):
     n[i][j] = int(input())
n2 = [[0 for i in range(c)] for j in range(r)]
print('Enter matrix 2 elements')
for i in range(r):
 for j in range(c):
     n2[i][j] = int(input())
for i in range(r):
 for j in range(c):
     n[i][j] += n2[i][j]
print('The sum of matrix is: ')
for i in range(r):
 for j in range(c):
    print(n[i][j], end=' ')
 print()