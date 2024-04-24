def fibonacci():
    cache = {}  # Cache to store the Fibonacci numbers

    def fib(n):
        if n in cache:  # Return the cached result if it exists
            return cache[n]
        if n <= 1:  # Base case for the Fibonacci sequence
            return n
        else:  # Recursive case
            result = fib(n - 1) + fib(n - 2)
            cache[n] = result  # Store the result in the cache
            return result

    return fib  # Return the recursive function

# Now we can create an instance of the memoized Fibonacci function
memoized_fibonacci = fibonacci()

# Example usage (no stdin/stdout required as per the problem statement):
# print(memoized_fibonacci(10))  # Should print 55
