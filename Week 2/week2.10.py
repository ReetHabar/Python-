# Input the number
number = int(input("Enter a number to find the sum of its digits: "))
sum_of_digits = 0

# Calculate the sum of digits
while number > 0:
    sum_of_digits += number % 10
    number //= 10

# Print the result
print("The sum of the digits is:", sum_of_digits)
