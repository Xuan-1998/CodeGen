def fibonacci(n, _cache={0: 0, 1: 1}):
    # Check if the result is already cached
    if n in _cache:
        return _cache[n]

    # Compute the Fibonacci number and cache it
    _cache[n] = fibonacci(n - 1, _cache) + fibonacci(n - 2, _cache)
    return _cache[n]

# Example usage (this part is just for demonstration and not part of the required solution)
if __name__ == "__main__":
    n = int(input("Enter a number to compute its Fibonacci: "))
    print(f"The Fibonacci number for {n} is {fibonacci(n)}.")
