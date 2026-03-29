import sys

# Function to check if an integer is a prime or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if an integer is a good prime or not (based on the set of bad primes)
def is_good_prime(n, bad_primes):
    for prime in bad_primes:
        if n % prime == 0:
            return False
    return True

# Main function
def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = set(map(int, input().split()))

    # Initialize the table with zeros
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Fill the table from left to right and top to bottom
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            # Check if the last element is a good prime or not
            if is_good_prime(arr[j - 1], bad_primes):
                dp[i][j] = max(dp[i][j-1], 1 + dp[i-1][j-1]) if i > 0 else 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1])

    # Print the maximum beauty value of the entire array
    print(max(max(row) for row in dp))

solve()
