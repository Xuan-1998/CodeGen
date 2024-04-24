def fibonacci(n, memo=None):
    if memo is None:
        memo = {}  # Initialize the cache when the function is first called
    
    if n in memo:
        return memo[n]  # Return the cached result if it exists
    
    if n <= 2:
        return 1  # Base cases for the first two Fibonacci numbers
    
    # Recursive calculation with memoization
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    
    return memo[n]

# Example usage:
# Read an integer from stdin
n = int(input("Enter the Fibonacci sequence number to calculate: "))
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
