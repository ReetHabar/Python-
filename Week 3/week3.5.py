n = int(input("Enter the number of terms for the series: "))
print("Series:", end=" ")
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    print(factorial, end=" ")
