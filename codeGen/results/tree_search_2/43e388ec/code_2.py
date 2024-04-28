import sys

# Define the modulo value
MOD = 10**9 + 7

def solve():
    # Read input values for 'a' and 'b'
    a, b = map(int, input().split())

    # Initialize DP table
    dp = [[0] * (b.bit_length() + 1) for _ in range(315)]

    # Base case: i > 314159
    for i in range(b.bit_length(), -1, -1):
        mask = ((1 << i) - 1)
        dp[0][i] = pow(2, i, MOD)

    # Fill up the DP table using dynamic programming
    for i in range(1, 315 + 1):
        for j in range(b.bit_length(), -1, -1):
            mask = ((1 << j) - 1)
            dp[i][j] = (dp[i-1][j] if j >= i.bit_length() else 0) + dp[0][i.bit_length()]
            if a & (mask << i.bit_length()):
                dp[i][j] += dp[i-1][j]
            if b & (mask << j):
                dp[i][j] = (dp[i][j] * 2) % MOD
            if dp[i][j] >= MOD:
                dp[i][j] -= MOD

    # Calculate the sum modulo 10^9+7
    total_sum = sum(dp[i][i.bit_length()] for i in range(315 + 1))
    print(total_sum % MOD)

if __name__ == "__main__":
    solve()
