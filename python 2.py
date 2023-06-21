def fibonacci(n):
    fib_sequence = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers

    if n <= 0:
        return []

    if n == 1:
        return [0]

    if n == 2:
        return fib_sequence

    for i in range(2, n):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)

    return fib_sequence

# Prompt the user for the number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Call the fibonacci function and store the result
fib_numbers = fibonacci(n)

# Print the Fibonacci numbers
print("Fibonacci sequence:")
for number in fib_numbers:
    print(number)
