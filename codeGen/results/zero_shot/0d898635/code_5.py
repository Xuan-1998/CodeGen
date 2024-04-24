def fibonacci_memoization():
    cache = {}  # Cache to store the Fibonacci numbers

    def fib(n):
        if n in cache:  # Check if fib(n) is already in the cache
            return cache[n]
        if n <= 1:  # Base case: fib(0) = 0, fib(1) = 1
            return n
        else:  # Recursive case: Calculate the nth Fibonacci number
            cache[n] = fib(n - 1) + fib(n - 2)  # Store the result in the cache
            return cache[n]

    return fib  # Return the fib function with the cache

# Create a memoized Fibonacci function
memoized_fib = fibonacci_memoization()

# Example usage (you can replace these lines with code to read from stdin)
n = int(input("Enter the value of n: "))
print(f"The {n}th Fibonacci number is: {memoized_fib(n)}")
