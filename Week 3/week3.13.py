n = int(input("Enter the number of terms for the series: "))
sum_series = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_series -= 1 / i
    else:
        sum_series += 1 / i
print("The sum of the series up to", n, "terms is:", sum_series)
