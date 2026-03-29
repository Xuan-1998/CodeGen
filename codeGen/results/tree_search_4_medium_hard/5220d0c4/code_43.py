def max_beauty(A, primes):
    n = len(A)
    m = len(primes)

    # Initialize Beauty table with zeros
    Beauty = [[0] * (n + 1) for _ in range(n + 1)]

    # Fill the table using dynamic programming
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            good_primes = sum(1 if p not in primes else -1 for k, p in enumerate(prime_factors(A[k])) for k in range(j))
            Beauty[i][j] = max(Beauty[i-1][j], Beauty[i][j-1]) + (good_primes > 0) * 1

    # Return the maximum beauty value
    return max(max(row) for row in Beauty)

# Define a helper function to calculate prime factors
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Example usage
A = [12, 15, 20]  # Input array
primes = [2, 3, 5]  # Bad prime numbers
print(max_beauty(A, primes))  # Output: Maximum beauty value for the input array
