from sys import stdin

def solve():
    n, m = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))
    bad_primes = list(map(int, stdin.readline().split()))

    # Create a 2D memoization table with (n+1) rows and (m+1) columns
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: the maximum beauty value for an empty array is 0
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr[i - 1] == bad_primes[j - 1]:
                # If the current number is a bad prime, update the state based on three cases
                dp[i][j] = min((i - 1, n - 1), (i - 1, j - 1), dp[i - 1][j - 1] + (-1 if arr[i - 1] in bad_primes else 1))
            else:
                # If the current number is a good prime, increment the beauty value by 1
                dp[i][j] = dp[i - 1][j - 1] + (1 if arr[i - 1] not in bad_primes else -1)

    return max(max(row) for row in dp)

print(solve())
