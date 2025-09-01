number = int(input("Enter a number to check if it is a Krishnamurthy number: "))
temp = number
sum_of_factorials = 0
while temp > 0:
    digit = temp % 10
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    sum_of_factorials += factorial
    temp //= 10
if sum_of_factorials == number:
    print("The number is a Krishnamurthy number.")
else:
    print("The number is not a Krishnamurthy number.")
