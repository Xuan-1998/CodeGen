from sys import stdin

n, m = map(int, stdin.readline().split())
edges = [list(map(int, stdin.readline().split())) for _ in range(m)]
k = int(stdin.readline())
p = list(map(int, stdin.readline().split()))

dp = [[0, 0] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(k-1, -1, -1):
        if p[j] == p[k-1]:
            break
        dp[i][0] = min(dp[j-1][0], 1) + abs(p[j]-p[j-1])
        dp[i][1] = max(dp[j-1][1], 1)

print(f"{dp[n][0]} {dp[n][1]}")
