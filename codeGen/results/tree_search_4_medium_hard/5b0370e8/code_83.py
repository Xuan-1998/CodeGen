import sys

MOD = 10**9 + 7

def solve():
    n, k = map(int, input().split())
    dp = [[0] * (1 << k) for _ in range(1 << k)]

    # Initialize the base case: all numbers less than or equal to 2^k have a bitwise AND of at least j
    for i in range(1 << k):
        for j in range(i + 1):
            dp[i][j] = 1

    for i in range(1 << k):
        for j in range(min(i, (1 << k) - 1)):
            if i & j:  # Check if the bitwise AND of i and j is greater than or equal to j
                dp[i][j] = 0
            else:
                dp[i][j] = 1

    result = sum(1 for i in range(1 << k) if dp[i][i])
    print(result % MOD)

if __name__ == "__main__":
    solve()
