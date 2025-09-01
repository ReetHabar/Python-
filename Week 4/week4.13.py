l = int(input("Enter the maximum width of the diamond (odd number): "))
for i in range(1, l + 1, 2):
    print(' ' * ((l - i) // 2), end='') 
    for j in range(1, i + 1):
        print(j, end='')
    print()
for i in range(l - 2, 0, -2):
    print(' ' * ((l - i) // 2), end='')
    for j in range(1, i + 1):
        print(j, end='')
    print()
