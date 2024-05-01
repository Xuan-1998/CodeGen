import math

def min_squares(n, m):
    # Calculate the smallest common multiple of n and m
    lcm = n * m // math.gcd(n, m)

    # Initialize the minimum number of squares
    min_squares = 0

    # Try smaller squares until we find one that fits or reach the base case
    while n > 1 and m > 1:
        square_size = math.isqrt(lcm)
        if lcm % square_size == 0:
            min_squares += 1
            lcm //= square_size ** 2
        else:
            # If we can't find a square that fits, increment the minimum number of squares
            min_squares += 1
            n -= 1
            m -= 1

    return min_squares + (n > 0) + (m > 0)

# Example usage:
n = int(input())
m = int(input())
print(min_squares(n, m))
