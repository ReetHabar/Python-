l = int(input("Enter the number of rows: "))
for i in range(1, l + 1):
    print(' ' * (l - i), end='')
    for j in range(i,0, -1):
        print(j, end='')
    for j in range(2, i + 1):
        print(j, end='')
    print()
