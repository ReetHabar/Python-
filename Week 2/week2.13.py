# Input the decimal number
decimal = int(input("Enter a decimal number to convert to binary: "))
binary = ""

# Convert to binary
while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal //= 2

# Display the binary number
print("Binary representation:", binary)
