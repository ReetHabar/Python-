def reet(n,m):
    if n==0:
        return 1
    else:
        return n*reet(n-1)
n=int(input("Enter any number"))
m=int(input("Enter the value of m"))
print(reet(n))
reet(n,m)
if (m==0):
    print(m+1)
n=24
m=36 
reet(n,m)
if m==0:
    return n
else:
    return reet(n,m%n)
def reet


