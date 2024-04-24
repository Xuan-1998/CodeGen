def generate_fibonacci(N):
    # Base cases
    if N == 1:
        return [1]
    elif N == 2:
        return [1, 1]
    
    # Initialize the list with the first two numbers
    fibonacci = [1, 1]
    
    # Calculate the remaining Fibonacci numbers
    for i in range(2, N):
        next_number = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_number)
    
    return fibonacci

def main():
    # Read the input from standard input
    N = int(input().strip())
    
    # Generate the first N Fibonacci numbers
    fibonacci_numbers = generate_fibonacci(N)
    
    # Print the Fibonacci numbers to standard output
    for number in fibonacci_numbers:
        print(number, end=' ')

if __name__ == "__main__":
    main()
