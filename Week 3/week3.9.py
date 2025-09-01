count = 0
sum_of_numbers = 0

while True:
    number = int(input("Enter an integer (0 to stop): "))
    if number == 0:
        break
    sum_of_numbers += number
    count += 1
if count > 0:
    average = sum_of_numbers / count
    print("The average of the entered numbers is:", average)
else:
    print("No numbers were entered.")
