import sys

def calculate_probability(n, m, h, s):
    dp = [0.0] * (n + 1)
    for i in range(m):
        if i == h:
            continue
        if s[i] >= n // m:
            for j in range(n, -1, -1):
                dp[j] = max(dp[j], min(1, (j + 1) / n))
        else:
            break
    return dp[n]

n, m, h = map(int, input().split())
s = list(map(int, input().split()))
if s[h] >= n // m:
    print(calculate_probability(n, m, h, s))
else:
    print(-1)
