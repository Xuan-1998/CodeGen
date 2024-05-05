from collections import defaultdict

def Treeland(n, roads):
    g = defaultdict(list)
    for si, ti in roads:
        g[si].append(ti)

    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    for i in range(2, n + 1):
        for j in g[i]:
            dp[i] = min(dp[i], dp[j] + 1)

    max_reversals = max(dp[2:])
    capitals = [i for i in range(2, n + 1) if dp[i] == max_reversals]
    print(max_reversals)
    print(*capitals)

n = int(input())
roads = []
for _ in range(n - 1):
    si, ti = map(int, input().split())
    roads.append((si, ti))

Treeland(n, roads)
