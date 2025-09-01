#W.P.P that prompts the user to input principle,rate,and time and calculate compound interest.
principle=float(input("Enter the Principle amount:"))
rate=float(input("Enter the Rate amount:"))/100
time=int(input("Enter the time  in year:"))
n=int(input("Enter the number of times interest is compound per year:"))
total_ammount=(principle*(1+rate/n))**(n*time)
compound_interest=(total_ammount-principle)
print("The compound interest is:",compound_interest )
print("The total Amount is:",total_ammount)
