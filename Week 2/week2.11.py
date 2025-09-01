# Input the number
number = int(input("Enter a number to reverse: "))
reversed_number = 0

# Reverse the number
while number > 0:
    remainder = number % 10
    reversed_number = reversed_number * 10 + remainder
    number //= 10

# Display the reversed number
print("Reversed number:", reversed_number)
