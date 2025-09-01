#W.P.P to input 3 number separated by comma,and find the largest and smallest among them
nums = list(map(int, input("Enter three numbers separated by spaces: ").split(",")))
larger_number=max(nums)
smallest_num=min(nums)
print("THe largest number is:",larger_number)
print("THe smallest number is:",smallest_num)