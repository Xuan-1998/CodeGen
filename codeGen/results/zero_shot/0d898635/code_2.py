def fibonacci(n, _cache={0: 0, 1: 1}):
    # Check if the value is already in the cache
    if n in _cache:
        return _cache[n]
    
    # Compute the Fibonacci number and add it to the cache
    _cache[n] = fibonacci(n - 1, _cache) + fibonacci(n - 2, _cache)
    return _cache[n]

# Example usage (uncomment to test):
# n = int(input("Enter the Fibonacci index: "))
# print(f"The Fibonacci number at index {n} is {fibonacci(n)}")
