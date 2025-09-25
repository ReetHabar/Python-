def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

def recursive_calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    
    result = calculate(a, b, operation)
    print("The result is:", result)
    
    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() == 'yes':
        recursive_calculator()

recursive_calculator()
// you can also used eval()
//function to creat a calculator 