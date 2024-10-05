#index of first fibonacci number with x digits
fibonacci_sequence = [1, 1]
index_found = False
digits = int(input("Number of digits to check for: "))

def check_digits(x):
    global index_found
    if len(str(fibonacci_sequence[-1])) >= x:
        print(f'Index: {fibonacci_sequence.index(fibonacci_sequence[-1])+1}')
        print(f'Number: {fibonacci_sequence[-1]}')
        index_found = True
        return index_found

def fibonaccize(n):
    global index_found
    list_length = len(fibonacci_sequence)
    new_fibonacci = fibonacci_sequence[list_length-1] + fibonacci_sequence[list_length-2]
    fibonacci_sequence.append(new_fibonacci)
    check_digits(n)

while index_found != True:
    fibonaccize(digits)