n = int(input("Enter the number of lines: "))
for i in range(1, n+1):
    num = 1 
    for k in range(n-i):
     print(" ",end="")
    for j in range(1, i+1):
        print(num,end=" ")
        num = num * (i - j) // j
    print()