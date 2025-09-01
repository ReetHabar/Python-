import datetime

date_input = input("Enter a date (mm/dd/yyyy): ")
date_obj = datetime.datetime.strptime(date_input, "%m/%d/%Y")
formatted_date = date_obj.strftime("%B %d, %Y")
print("Formatted date:", formatted_date)
