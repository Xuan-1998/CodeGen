import sys; input = lambda: [int(x) for x in input().split()]
n, portals = *input(), []
for _ in range(n):
    p = next(input())
    portals.append(p)
dp = {1: 0}
for i in range(2, n+1):
    dp[i] = sys.maxsize
dp[n+1] = 0
for i in range(1, n+1):
    if i not in dp:
        continue
    p_i = portals[i-1]
    dp[i] = min(dp[i], dp[p_i] + (i % 2 and 1 or 0))
print((dp[n+1] + 1) % (10**9 + 7))
