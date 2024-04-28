from sys import stdin

def dp(s):
    n = len(s)
    dp = [False] * (n + 1)

    dp[0] = True
    for i in range(1, n + 1):
        if s[i - 1:i + 1] in ['AB', 'BA']:
            dp[i] = any(dp[j] for j in range(i) if s[i - j:i + j] in ['AB', 'BA'])
        else:
            dp[i] = dp[i - 1]

    return 'YES' if any(dp[i] for i in range(n)) else 'NO'

s = stdin.readline().strip()
print(dp(s))
