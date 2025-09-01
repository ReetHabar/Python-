l = int(input("Enter any number : "))
for i in range(1, l + 1):
    print(' ' * (l - i) + '*' * (2 * i-1 ))