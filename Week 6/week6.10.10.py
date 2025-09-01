m = ["January", "February", "March", "April", "May", "June", "July", "August",
"September", "October", "November",
 "December"]
n = input("Enter a date (mm/dd/yyyy): ")
mm, d, y = (int(i) for i in n.split('/'))
if (1 <= mm <= 12 and
 ((mm == 2 and ((d <= 29 and (y % 4 == 0 and y % 100 != 0 or y % 400 == 0)) or
(d <= 28))) or
 (d <= 31 and mm in [1, 3, 5, 7, 8, 10, 12]) or
 (d <= 30 and mm in [4, 6, 9, 11]))):
 print(f"Formatted date: {m[mm - 1]} {d}, {y}")
else:
 print("Invalid date.")