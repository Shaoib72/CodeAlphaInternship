
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence

# Example usage:
number = int(input("Enter a number to generate Fibonacci sequence up to that number: "))
fibonacci_sequence = generate_fibonacci(number)
print("Fibonacci sequence up to", number, ":", fibonacci_sequence)
