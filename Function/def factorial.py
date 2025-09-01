# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# number = 5
# print(f"Factorial of {number} without recursion is: {factorial(number)}")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number = 5
print(f"Factorial of {number} using recursion is: {factorial(number)}")
