import math

def odd_divisors(N):
    # Count all perfect squares up to N
    perfect_squares = [i**2 for i in range(1, int(math.sqrt(N)) + 1)]

    # Subtract duplicates (numbers that are both perfect squares and also a power of another number)
    duplicates = set([i for i in perfect_squares if any(j*j == i for j in range(1, int(i**0.5) + 1))])
    count = len(perfect_squares) - len(duplicates)

    return count

# Read input from stdin
N = int(input())

# Print the result to stdout
print(odd_divisors(N))
