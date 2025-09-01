n = int(input("Enter the number of terms for the series: "))
print("Series:", end=" ")
term = 1
add_value = 1
for i in range(n):
    print(term, end=" ")
    if i < 4:
        term *= 2
    else:
        term += add_value
        add_value += 2
