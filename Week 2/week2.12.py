# Input the number of terms
n = int(input("Enter a number to find the sum of squares of the first n natural numbers: "))
sum_of_squares = 0

# Calculate the sum of squares
for i in range(1, n + 1):
    sum_of_squares += i * i

# Display the result
print("The sum of squares of the first", n, "natural numbers is:", sum_of_squares)
