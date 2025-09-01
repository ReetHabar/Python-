n=int(input('enter any number='))
t=[[1]*(i+1)for i in range(n)]
for i in range (2,n):
    for j in range(1,i):
        t[i][j]=t[i-1][j-1]*t[i-1][j]
for row in t:
    print(''.join(map(str,row)).center(n*2))        