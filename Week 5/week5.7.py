# Program to check if a string is a palindrome
string = input("Enter a string: ")
is_palindrome = string == string[::-1]

if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# Program to display shifting pattern
word = "SHIFT"
for i in range(len(word)):
    print(word[i:] + word[:i])


# Program to validate a password based on certain requirements
password = input("Enter a password: ")

if (len(password) >= 8 and 
    any(char.isupper() for char in password) and
    any(char.islower() for char in password) and
    any(char.isdigit() for char in password)):
    print("Password is valid.")
else:
    print("Password is invalid. It must be at least 8 characters long, "
          "contain at least one uppercase letter, one lowercase letter, and one digit.")


# Program to check if an arithmetic expression has balanced parentheses
expression = input("Enter an arithmetic expression: ")
stack = []
balanced = True

for char in expression:
    if char == '(':
        stack.append(char)
    elif char == ')':
        if stack:
            stack.pop()
        else:
            balanced = False
            break

if balanced and not stack:
    print("The arithmetic expression is correct (parentheses are balanced).")
else:
    print("The arithmetic expression is incorrect (parentheses are not balanced).")
