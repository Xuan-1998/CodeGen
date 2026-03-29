import sys

def calculate_probability():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    dp = [[0.0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(m + 1):
        if i == 0:
            dp[0][i] = 1.0
        else:
            for k in range(1, n + 1):
                if k < s[i - 1]:
                    dp[k][i] = dp[k][i - 1]
                else:
                    dp[k][i] = max(dp[k-1][i], (s[i-1] / (n + h - 1)) * dp[k-1][i-1])
    
    if n < sum(s):
        return -1.0
    else:
        return dp[n][h]

print(calculate_probability())
