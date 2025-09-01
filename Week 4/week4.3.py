n=int(input("Enter any number="))
m=[[0]* n for i in range(n)]
num,t,b,l,r,=1,0,n-1,0,n-1
while t<=b and 1<=r:
    for i in range(1,r+1): 
        m[t][i]=num,
    num+=1
    t+=1
    for i in range(t,b+1):
        m[i][r]=num,
    num+=1
    r-=1
    for i in range(r,l-1,-1):
        m[b][i]=num,
    num+=1
    b-=1
    for i in range(b,t-1,-1):
        m[i][l]=num,
    num +=1
    l+=1
    for row in m:
        print(''.join(map(str,row)))