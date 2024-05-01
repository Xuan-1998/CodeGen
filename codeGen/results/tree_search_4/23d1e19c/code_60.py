import sys

def main():
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
    
    k = int(input())
    path = list(map(int, input().split()))
    dp = [[-sys.maxsize, -sys.maxsize] for _ in range(n)]

    def dfs(v):
        if dp[v][0] != -sys.maxsize:
            return dp[v]
        
        if v == path[-1]:
            dp[v] = [0, 0]
            return dp[v]

        for next_v in graph.get(v, []):
            dist = dfs(next_v)[0]
            if dist + 1 <= k and (dp[next_v][0] < -sys.maxsize or dist + 1 < dp[next_v][0]):
                dp[v] = [dist + 1, min(dp[next_v][1], dist + 1)]
            elif dist + 1 > k:
                dp[v] = [max(dp[v][0], dist), max(dp[v][1], dist)]

        return dp[v]

    dfs(path[0])
    print(min(max(dp[-1])))

if __name__ == "__main__":
    main()
