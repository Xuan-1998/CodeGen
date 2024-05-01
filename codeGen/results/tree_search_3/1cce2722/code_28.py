import sys

def dp_solutions(n, seq):
    # Initialize the DP table with zeros
    dp = [[0] * n for _ in range(n)]

    # Base cases: dp[i][k] = 0 for all k and dp[i][i] = i for all i
    for i in range(n):
        dp[i][i] = i

    # Fill the DP table row by row or column by column
    for i in range(1, n):
        for j in range(i + 1):
            if seq[j] == i:  # If there's no more points to earn after current element
                dp[i][j] = i - 1
            else:
                # Consider deleting elements equal to ak + 1 and ak - 1
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j+1]) if j > 0 and j < n - 1 else i - 1

    return dp[n-1][n//2] if n % 2 == 0 else dp[n-1][n//2 + 1]

# Read input
n = int(input())
seq = list(map(int, input().split()))

print(dp_solutions(n, seq))
