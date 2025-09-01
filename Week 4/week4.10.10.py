n=int(input("Enter any number="))
for i in range(1,n+1):
    for i in range(n-1):
        print('',end='')
    for k in range(2*i):
        print('*',end='')
        print()