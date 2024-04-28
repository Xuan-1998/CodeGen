from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    s, t, k = map(int, input().split())
    path = list(map(int, input().split()))

    memo = {}

    def dfs(v):
        if (v,) in memo:
            return memo[(v,)]
        
        if v == t:
            return [0, 0]

        dp = [float('inf'), -1]
        for p in range(k):
            next_v = path[p]
            if graph[next_v]:
                for neighbor in graph[next_v]:
                    if (neighbor,) not in memo:
                        result = dfs(neighbor)
                        dp[0] = min(dp[0], 1 + result[0])
                        dp[1] = max(dp[1], 1 + result[1])
            else:
                dp[0] = 0
                dp[1] = 0
        memo[(v,)] = dp
        return dp

    print(dfs(s))

