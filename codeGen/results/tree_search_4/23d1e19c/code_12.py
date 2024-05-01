import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    k = int(input())
    path = list(map(int, input().split()))
    dp = [[0, 0] for _ in range(n+1)]

    def dfs(i, j):
        if i == n:
            return [dp[j][0], dp[j][1]]
        
        if dp[i][j] != (0, 0):
            return dp[i][j]

        if path[j-1] == i:
            next_min, next_max = dfs(i+1, j)
            dp[i][j] = [next_min, next_max]
        else:
            next_min, next_max = sys.maxsize, -sys.maxsize
            for neighbor in graph[i]:
                if neighbor < path[j-1]:
                    next_min, _ = min((dfs(neighbor+1, j)[0], dfs(neighbor+1, j)[1]), default=(next_min, next_max))
                    _ , next_max = max((dfs(neighbor+1, j)[0], dfs(neighbor+1, j)[1]), default=(next_min, next_max))
            dp[i][j] = [next_min+1, next_max+1]

        return dp[i][j]

    print(max(dfs(0, k)) - min(dfs(0, k)))

if __name__ == "__main__":
    solve()
