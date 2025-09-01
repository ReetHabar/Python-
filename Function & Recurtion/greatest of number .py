#WAP a using function to find greatest of three number.
def reet(a,b,c):
    return max(a,b,c)
a=int(input("enter any number a="))
b=int(input("enter any number b="))
c=int(input("enter any number c="))
print("the greatest number is",reet(a,b,c))


a = list(map(int, input("Enter numbers separated by spaces: ").split()))
greatest = max(a)
print("the greatest number is ",greatest)