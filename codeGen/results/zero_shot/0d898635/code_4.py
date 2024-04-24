def fibonacci(n, _cache={}):
    # Base cases
    if n == 0: return 0
    if n == 1: return 1
    
    # Check if the result is already cached
    if n in _cache:
        return _cache[n]
    
    # Compute the Fibonacci number and cache it
    _cache[n] = fibonacci(n - 1, _cache) + fibonacci(n - 2, _cache)
    return _cache[n]

# Example usage (not required by the problem statement)
# Read an integer from standard input and print the nth Fibonacci number
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
