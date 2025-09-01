#W.P.P to find the roots of a quadratic equation using Python.
import math

# coefficients a, b, and c
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# calculate discriminant
D = b**2 - 4*a*c

# check if roots are real or complex
if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("Two Real and Distinct Roots:", root1, "and", root2)
elif D == 0:
    root = -b / (2*a)
    print("One Real and Equal Root:", root)
else:
    real_part = -b / (2*a)
    imag_part = math.sqrt(-D) / (2*a)
    print("Two Complex Roots:")
    print(f"{real_part} + {imag_part}i and {real_part} - {imag_part}i")
