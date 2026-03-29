import sys

def update_dp(dp, t, s):
    n = len(s)
    for i in range(n):
        pos = t.find(s[i])
        while pos != -1:
            dp[pos] = min(dp.get(pos, 0) + 1, dp.get(pos + len(s[i]), 0) if pos + len(s[i]) < len(t) else 1)
            pos = t.find(s[i], pos + 1)

dp = {}
t = input().strip()
n = int(input())
for i in range(n):
    s.append(input().strip())

m = float('inf')
for i in range(len(t)):
    m = min(m, dp.get(i, 0) if i < len(t) else 1)
if m == float('inf'):
    print(-1)
else:
    for _ in range(m):
        pos = max((i for i in dp if dp[i] == m - _), default=-1)
        print(pos + 1, end=' ')
    print()
