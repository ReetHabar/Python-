import math
sum_series = 0
for i in range(1, 8):
    term = i / math.factorial(i)
    sum_series += term
print("The sum of the first seven terms of the series is:", sum_series)
