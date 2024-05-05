import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    # Precompute prime divisors for memoization
    prime_divisors = defaultdict(dict)
    for i in range(2, max(arr) + 1):
        if i not in bad_primes:
            j = 2
            while i * j <= max(arr):
                prime_divisors[j][i] = i // (i % j)
                j += 1

    # Initialize the table with a dummy value for the base case
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(2, n + 1):
        dp[i][i] = arr[i - 1]

    for length in range(3, n + 1):
        for left in range(n - length + 1):
            right = left + length
            good_prime = all(p not in bad_primes for p in prime_divisors[arr[left - 1]].values())
            if good_prime:
                dp[left][right] = dp[left][left]
            else:
                min_beauty = float('inf')
                for i in range(left, right):
                    min_beauty = min(min_beauty, dp[left][i])
                    prime_divisor = arr[i] // (arr[i] % (arr[right - 1] // (arr[right - 1] % arr[i])))
                    if prime_divisor not in bad_primes:
                        min_beauty = min(min_beauty, dp[left][right - 1] + prime_divisor)
                dp[left][right] = min_beauty

    print(dp[0][n - 1])

if __name__ == "__main__":
    solve()
