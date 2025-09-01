# Prompt the user to enter the number of calls
try:
    calls = int(input("Enter the number of calls made: "))
    
    # Calculate the bill based on the number of calls
    if calls <= 100:
        bill = 200  # Minimum bill for up to 100 calls
    elif calls <= 150:
        bill = 200 + (calls - 100) * 0.60  # 0.60 per call for the next 50 calls
    elif calls <= 200:
        bill = 200 + (50 * 0.60) + (calls - 150) * 0.50  # 0.50 per call for the next 50 calls
    else:
        bill = 200 + (50 * 0.60) + (50 * 0.50) + (calls - 200) * 0.40  # 0.40 per call beyond 200 calls

    # Display the total bill
    print(f"The total telephone bill is: Rs. {bill:.2f}")

except ValueError:
    print("Invalid input. Please enter a valid number of calls.")
