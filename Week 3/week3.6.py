n = int(input("Enter a positive integer N: "))
sum_reciprocals = 0
for i in range(1, n + 1):
    sum_reciprocals += 1 / i
print("The sum of reciprocals from 1 to", n, "is:", sum_reciprocals)
