
36#W.P.P to calculate the area and perimeter of various polygons such as triangles,rectangles,and circle.
import math
def calculate_triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    side1 = float(input("Enter the first side of the triangle: "))
    side2 = float(input("Enter the second side of the triangle: "))
    side3 = float(input("Enter the third side of the triangle: "))
    area = 0.5 * base * height
    perimeter = side1 + side2 + side3
    print(f"Triangle - Area: {area}, Perimeter: {perimeter}")

def calculate_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    perimeter = 2 * (length + width)
    print(f"Rectangle - Area: {area}, Perimeter: {perimeter}")

def calculate_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius * radius
    perimeter = 2 * math.pi * radius
    print(f"Circle - Area: {area}, Perimeter: {perimeter}")

def main():
    print("Choose the polygon:")
    print("1. Triangle")
    print("2. Rectangle")
    print("3. Circle")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        calculate_triangle()
    elif choice == '2':
        calculate_rectangle()
    elif choice == '3':
        calculate_circle()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
