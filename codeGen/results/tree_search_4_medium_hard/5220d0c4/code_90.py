def max_beauty(arr, bad_primes):
    n = len(arr)
    m = len(bad_primes)

    # Initialize a 2D table with shape (n+1, m+1) for storing dynamic programming values
    dp = [[-float('inf')] * (m + 1) for _ in range(n + 1)]

    # Fill the table from left to right, top to bottom
    for i in range(1, n + 1):
        for j in range(m + 1):
            last_elem = arr[i - 1]

            # Consider two possibilities: either the last element is a good prime or not
            if is_good_prime(last_elem):
                # If it's a good prime, update the beauty value considering minimum prime divisor and bad prime status
                dp[i][j] = max(dp[i][j], min_prime_divisor(last_elem) + (1 if j == 0 else -1))
            else:
                # If it's not a good prime, consider two more possibilities: either last element is a bad prime or not
                if last_elem in bad_primes:
                    dp[i][j] = max(dp[i][j], min_prime_divisor(last_elem) + (1 if j == 0 else -1))
                else:
                    # If it's not a bad prime, simply propagate the beauty value from previous cell
                    dp[i][j] = dp[i - 1][j]

    return dp[n][m]


def is_good_prime(n):
    """Check if n is a good prime number"""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def min_prime_divisor(n):
    """Find the minimum prime divisor of n"""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and is_prime(i):
            return i

    return n


def is_prime(n):
    """Check if n is a prime number"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    print(max_beauty(arr, bad_primes))
