def fibonacci(n):
    # Initialize the memoization cache as a dictionary
    memo = {}

    def fib_helper(x):
        # If the value is already in the cache, return it
        if x in memo:
            return memo[x]
        # Base cases for the recursion
        if x == 0:
            return 0
        if x == 1:
            return 1
        # Calculate the Fibonacci number recursively
        result = fib_helper(x - 1) + fib_helper(x - 2)
        # Store the result in the cache before returning
        memo[x] = result
        return result

    # Call the helper function
    return fib_helper(n)

# Example usage (not part of the solution as no input/output is required):
# print(fibonacci(10))  # Should print 55
