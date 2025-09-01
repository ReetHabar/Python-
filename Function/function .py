# def india(wb="west bengal"):
#     print("we are from"+wb)
# state =india  
def week(a):
  if a==1:
      print("Monday")
  elif a==2:
      print("Tuesday")
  elif a==3:
      print("Wednesday")
  elif a==4:
      print("Thrusday")
  elif a==5:
      print("Friday")
  elif a==6:
      print("Saturday")
  elif a==7:
      print("Sunday")
  else:
      print("Enter a correct value")
a=int(input("enter value"))
b=week(a)
print(b)