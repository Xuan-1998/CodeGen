from collections import defaultdict

def maxOrValue(n, s):
    dp = [[-1] * (n + 1) for _ in range(n + 1)]

    # Base case: single character
    for i in range(1, n + 1):
        dp[i][i] = int(s[i - 1], 2)

    # Fill the DP table
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length
            if s[i - 1] == '0':
                dp[i][j] = max(dp[k][j] for k in range(i))
            else:
                dp[i][j] = max(dp[k][j] for k in range(i)) | int(s[j - 1], 2)

    # Find the maximum OR value
    return str(max(dp[0][k] for k in range(n)))

n = int(input())
s = input().strip()

print(maxOrValue(n, s))
