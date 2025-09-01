n = int(input("Enter the number of terms for the series: "))
print("Series:", end=" ")
term = 2
for _ in range(n):
    print(term, end=" ")
    term *= 2
