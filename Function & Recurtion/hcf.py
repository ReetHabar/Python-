def hcf(a, b):
    while b:
        a, b = b, a % b
    return a


num1 = 24
num2 = 36
print("HCF:", hcf(num1, num2))

def lcm(a, b):
    return (a * b) // hcf(a, b)

num1 = 24
num2 = 36
print("LCM:", lcm(num1, num2))
