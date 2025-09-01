num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
first_term, second_term = 0, 1
for _ in range(1, num_terms):
        next_term = first_term + second_term
        print(next_term, end=" ")
        first_term, second_term = second_term, next_term
