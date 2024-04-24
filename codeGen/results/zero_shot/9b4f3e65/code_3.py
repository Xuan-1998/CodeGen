def generate_fibonacci(n):
    # The first two Fibonacci numbers
    fib = [1, 1]
    # Generate the Fibonacci sequence up to n
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]  # Return only the first n numbers

def main():
    # Read the input N
    n = int(input().strip())
    # Generate the first N Fibonacci numbers
    fibonacci_numbers = generate_fibonacci(n)
    # Print the Fibonacci numbers
    for num in fibonacci_numbers:
        print(num, end=' ')

if __name__ == "__main__":
    main()
