def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in cm: "))

bmi = calculate_bmi(weight, height)

print(f"Your BMI is: {bmi:.2f}")
print("BMI Classification:", classify_bmi(bmi))