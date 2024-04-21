def fibonacci(N):
    if N == 1:
        return [1]
    elif N == 2:
        return [1, 1]
    else:
        fib = [1, 1]
        for _ in range(N - 2):
            fib.append(fib[-2] + fib[-1])
        return fib

# Read input from stdin
N = int(input().strip())

# Calculate the first N Fibonacci numbers
fib_numbers = fibonacci(N)

# Print the result to stdout
print(fib_numbers)
