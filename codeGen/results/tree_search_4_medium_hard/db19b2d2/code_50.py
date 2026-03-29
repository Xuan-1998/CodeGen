import sys

n, m, h = map(int, input().split())
s = list(map(int, input().split()))

dp = [[-1.0 for _ in range(n+1)] for _ in range(m+1)]

for i in range(1, m+1):
    si = sum(s[j] for j in range(i))
    for k in range(min(n, si)):
        p1 = k / (s[i-1] if i > 0 else 0)
        p2 = 1 - p1
        dp[i][k] = max(p1, p2)

ans = max(dp[h])
print(ans if ans >= 0 else -1)
