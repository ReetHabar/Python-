number = int(input("Enter a number to print its multiplication table: "))
print("Multiplication Table of", number)
for i in range(1, 11):
    print(number, "x", i, "=", number * i)
