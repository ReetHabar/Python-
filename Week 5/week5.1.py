# 1. Program to count and display the number of vowels in a string
string = input("Enter a string: ")
vowels = 'aeiouAEIOU'
vowel_count = 0

for char in string:
    if char in vowels:
        vowel_count += 1

print("Number of vowels in the string:", vowel_count)


# 2. Program to display the count of uppercase, lowercase, digits, and whitespace in a string
string = input("Enter a string: ")
uppercase_count = 0
lowercase_count = 0
digit_count = 0
whitespace_count = 0

for char in string:
    if 'A' <= char <= 'Z':
        uppercase_count += 1
    elif 'a' <= char <= 'z':
        lowercase_count += 1
    elif '0' <= char <= '9':
        digit_count += 1
    elif char == ' ':
        whitespace_count += 1

print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)
print("Number of digits:", digit_count)
print("Number of whitespace characters:", whitespace_count)


# 3. Program to exchange the first and last characters of a string
string = input("Enter a string: ")

if len(string) > 1:
    new_string = string[-1] + string[1:-1] + string[0]
else:
    new_string = string  # If string is too short, no swapping needed

print("New string with first and last characters exchanged:", new_string)


# 4. Program to reverse the string
string = input("Enter a string: ")
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string  # Add each character at the start

print("Reversed string:", reversed_string)


# 5. Program to create a new string by shifting one position to the left
string = input("Enter a string: ")

if len(string) > 1:
    shifted_string = string[1:] + string[0]
else:
    shifted_string = string  # If string is too short, no shifting needed

print("New string after shifting left by one position:", shifted_string)


# 6. Program to print initials of the user's full name
full_name = input("Enter your full name (first middle last): ")
initials = ""

if len(full_name) > 0:
    initials += full_name[0].upper() + ". "  # First initial

    for i in range(1, len(full_name) - 1):
        if full_name[i] == ' ' and full_name[i+1] != ' ':
            initials += full_name[i+1].upper() + ". "  # Middle and last initials

print("Initials:", initials.strip())
