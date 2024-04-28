n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
p = list(map(int, input().split()))
dp = [float('inf')] * n
dp[0] = 0

for i in range(len(p)-1):
    for j in range(n):
        if dp[j] == float('inf'): continue
        if abs(j-p[i]) <= 2:
            dp[p[i+1]-1] = min(dp[p[i+1]-1], dp[j]+1)

print(min(dp), max(dp))
