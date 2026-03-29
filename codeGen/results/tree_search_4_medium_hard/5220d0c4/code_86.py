import heapq
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    # Create a dictionary to store minimum prime divisors for each number
    min_divisors = defaultdict(int)

    for p in range(2, 1000000):  # Assuming max number is 10^9
        if all(p % i > 0 for i in range(2, int(p**0.5) + 1)):
            min_divisors[p] = p

    for p in bad_primes:
        min_divisors[p] -= 1

    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        if arr[i] not in min_divisors:  # If the number is prime
            min_divisor = arr[i]
        else:
            min_divisor = min_divisors[arr[i]]

        if min_divisor > 0:  # The number is good prime
            dp[i] = max(dp[i], dp[i + 1] + min_divisor)
        else:
            dp[i] = max(dp[i], dp[i + 1] - min_divisor)

    print(max(dp))

if __name__ == "__main__":
    solve()
