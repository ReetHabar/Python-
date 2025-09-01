number = int(input("Enter a number to check if it is an Armstrong number: "))
num_str = str(number)
num_digits = len(num_str)
sum_of_powers = 0
for digit in num_str:
    sum_of_powers += int(digit) ** num_digits
if sum_of_powers == number:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
