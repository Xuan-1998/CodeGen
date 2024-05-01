import sys

def maximum_points(n, a):
    # Initialize DP table with zeros
    dp = [[0]*(n) for _ in range(n)]

    for i in range(1, n+1):
        for j in range(i-1, -1, -1):
            if a[i-1] == a[j-1] + 1 or a[i-1] == a[j-1] - 1:
                dp[i-1][j-1] = max(dp[i-1][j-1], dp[j-2][i-2] + 1)
            else:
                if i > j+1:
                    dp[i-1][j-1] = max(dp[i-1][j-1], dp[i-2][j-2])
                else:
                    dp[i-1][j-1] = 0

    return dp[n-1][n-2]

# Read input from stdin
n = int(input())
a = list(map(int, input().split()))

# Print the answer to stdout
print(maximum_points(n, a))
