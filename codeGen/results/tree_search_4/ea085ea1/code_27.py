import sys

def solve(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][k] for k in range(j))

    return dp[N][N]

# Read input from stdin
str1 = input().strip()
str2 = input().strip()

# Solve the problem and print the result to stdout
result = solve(str1, str2)
print(result)
