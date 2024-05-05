import sys

# Read input from stdin
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

memo = [(0, 0)] * (n + 1)  # Initialize memoization table


def calculate_beauty(i):
    if i < 0:
        return 0

    # Get the minimum prime divisor and whether it's a bad prime
    prime_divisor = min_prime_divisor(arr[i])
    is_bad_prime = prime_divisor in bad_primes

    # Calculate beauty value using memoization
    beauty = memo[i][1] if i > 0 else (0, 0)
    if is_bad_prime:
        beauty = max(beauty[0], calculate_beauty(i - 1)[1])
    else:
        beauty = (beauty[0] + 1, beauty[1])

    # Store the calculated beauty value in memoization table
    memo[i] = (beauty[0], beauty[1])

    return beauty


def min_prime_divisor(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return i

    return x


# Calculate and print the maximum beauty of the array
max_beauty = calculate_beauty(n - 1)[1]
print(max_beauty)
