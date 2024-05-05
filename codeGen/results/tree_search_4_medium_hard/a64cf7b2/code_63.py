# Read input
n, m, T = map(int, input().split())
dp = {}
for _ in range(m):
    u, v, t = map(int, input().split())
    dp[(u, v)] = t

# Initialize dp
dp[1] = {0: 1}
max_visit = 0
for i in range(2, n+1):
    for j in range(T+1):
        if (i-1, i) not in dp:
            dp[i] = {}
        dp[i][j] = max(dp.get((i-1, i), {t: 0}).get(j-t, 0), dp.get(i-1, {0: 0}).get(j, 0))
    if T > j and dp[i][j] > max_visit:
        max_visit = dp[i][j]

# Construct the optimal route
route = [n]
i = n
t = max_visit - 1
while i > 1:
    for edge in [(u, v) for (u, v), t in dp.items() if v == i]:
        if (edge[0], i) not in dp or t != dp[edge][j-t]:
            j -= dp[edge][j-t]
            break
    route.append(edge[0])
route.reverse()

# Print output
print(max_visit)
print(*route, sep='\n')
