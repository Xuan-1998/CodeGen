def memoized_fibonacci(n):
    memo = {}  # Cache to store Fibonacci numbers

    def fib(k):
        if k in memo:
            return memo[k]  # Return the cached result
        if k <= 1:
            return k  # Base cases: fib(0) = 0, fib(1) = 1
        result = fib(k-1) + fib(k-2)  # Recursive call
        memo[k] = result  # Cache the result for future use
        return result
    
    return fib(n)  # Call the helper function

# Example usage:
# Read an integer from stdin and print the nth Fibonacci number
if __name__ == "__main__":
    n = int(input().strip())
    print(memoized_fibonacci(n))
