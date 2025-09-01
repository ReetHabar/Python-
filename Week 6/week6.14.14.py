r, c = int(input('Enter mat 1 row length: ')), int(input('Enter mat 1 column length:'))
r2, c2 = int(input('Enter mat 2 row length: ')), int(input('Enter mat 2 column length:'))
if c == r2:
 n = [[0 for i in range(c)] for j in range(r)]
 print('Enter mat 1 elements')
 for i in range(r):
  for j in range(c):
     n[i][j] = int(input())
 n2 = [[0 for i in range(c2)] for j in range(r2)]
 print('Enter mat 2 elements')
 for i in range(r2):
    for j in range(c2):
      n2[i][j] = int(input())
 n3 = [[0 for i in range(c2)] for j in range(r)]
 for i in range(r):
     for j in range(c2):
        for k in range(r2):
            n3[i][j] += n[i][k] * n2[k][j]
 print('The multiplied matrix is: ')
 for i in range(r):
     for j in range(c2):
      print(n3[i][j], end=' ')
 print()
else:
 print('Not compatible for multiplication')