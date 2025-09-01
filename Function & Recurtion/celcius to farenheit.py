def faren(a):
    return ((a*9/5)+32)
a=float(input("enter a value"))
print(faren(a))


def celsius_to_fahrenheit( celsius):
    if  celsius == 0:
        return 32 
    else:
        return ((celsius * 9/5) + 32)
celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit=celsius_to_fahrenheit( celsius)
print(celsius_to_fahrenheit(celsius))




# def celsius_to_fahrenheit(celsius):
#     if celsius == 0:
#         return 32  
#     return ((celsius * 9/5) + 32)

# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = celsius_to_fahrenheit(celsius)
# print(f"{celsius}°C is equal to {fahrenheit}°F")
