positive_count = 0
negative_count = 0
zero_count = 0


while True:
    number = int(input("Enter a number (or type 'q' to quit): "))
    
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1
    continue_entry = input("Do you want to enter another number? (yes/no): ").strip().lower()
    if continue_entry != "yes":
        break
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Zeros:", zero_count)
