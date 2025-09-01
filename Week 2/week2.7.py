number = input("Enter a number to check if it is a palindrome: ")
if number == number[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
