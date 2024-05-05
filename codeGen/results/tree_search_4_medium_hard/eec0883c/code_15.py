from collections import defaultdict

def solve():
    n, *w = map(int, input().split())
    graph = defaultdict(list)
    for i in range(n-1):
        u, v, c = map(int, input().split())
        graph[u].append((v, c))
        graph[v].append((u, c))

    dp = [0] * (n+1)
    dp[1] = w[0]

    def dfs(city, remaining_gas):
        for neighbor, road_length in graph[city]:
            if road_length <= remaining_gas:
                dp[neighbor] = max(dp[neighbor], dfs(neighbor, remaining_gas - road_length))
        return dp[city]

    print(max(dfs(1, w[0]), key=int))

if __name__ == "__main__":
    solve()
