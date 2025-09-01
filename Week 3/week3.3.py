n = int(input("Enter the number of terms for the series: "))
print("Series:", end=" ")
term = 1
difference = 2
for _ in range(n):
    print(term, end=" ")
    term += difference
    difference += 2
