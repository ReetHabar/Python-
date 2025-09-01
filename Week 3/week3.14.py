x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms: "))
sin_x = 0
sign = 1
for i in range(1, 2 * n, 2):  
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    term = (x ** i) / factorial
    sin_x += sign * term
    sign *= -1
print("The computed value of sin(x) is:", sin_x)
