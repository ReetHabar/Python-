def get_day_of_week(day_number):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    return days.get(day_number, "Invalid input. Please enter a number between 1 and 7.")


try:
    day_number = int(input("Enter a number (1-7) to get the corresponding day of the week: "))
    
    print(get_day_of_week(day_number))

except ValueError:
    print("Invalid input. Please enter a valid number.")
