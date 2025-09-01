n = int(input("Enter the number of lines (N): "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("/", end="")
    
