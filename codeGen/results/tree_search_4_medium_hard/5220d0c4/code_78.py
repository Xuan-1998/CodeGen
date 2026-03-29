import heapq

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    good_primes = set()

    # Initialize the DP table
    for i in range(2, n):
        if all(arr[i] % p > 0 for p in bad_primes):
            good_primes.add(min([p for p in range(2, int(arr[i]**0.5) + 1) if arr[i] % p == 0]))
    dp[0][0] = 0

    # Fill the DP table
    for length in range(1, n):
        for i in range(length):
            if all(arr[i + j] % p > 0 for p in bad_primes) and min([p for p in range(2, int(arr[i + length]**0.5) + 1) if arr[i + length] % p == 0]) not in good_primes:
                dp[i][length] = max(dp[i][length], dp[i][length - 1])
            else:
                dp[i][length] = dp[i][length - 1]
    heapq.heapify([(-dp[0][n - 1],),])

    return abs(heapq.heappop()[0])
