import sys

n, m = map(int, input().split())
dp = [float('inf')] * n
species = {}

for i in range(n):
    s, x = map(int, input().split())
    species[s] = min(species.get(s, float('inf')), x)
    dp[i] = 0 if not species or x >= species[s] else sys.maxsize

for i in range(1, n):
    dp[i] += dp[i-1]
    for j in range(m):
        s = j + 1
        if x <= species.get(s, float('inf')):
            break
    for k in range(j+1, m):
        s = k + 1
        if species[s] > x:
            dp[i] += min(dp[k-1], sys.maxsize)
            break

print(min(dp))
