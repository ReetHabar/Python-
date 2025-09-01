number = int(input("Enter a positive integer: "))
sum_of_factors = 0
print("Factors of", number, "are:", end=" ")
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")
        sum_of_factors += i
print("\nThe sum of factors is:", sum_of_factors)
