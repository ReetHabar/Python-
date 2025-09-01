l = int(input("Enter the number of rows: "))
for i in range(1, l + 1):
    print(' ' * (l - i) + str(i) * (2 * i-1))