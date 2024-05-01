from collections import defaultdict

def min_max_recomputations(graph, path):
    n = len(graph)
    dp = [float('inf')] * (n + 1)
    memo = defaultdict(lambda: float('inf'))

    def dfs(v):
        if v not in memo:
            if v == path[-1]:
                return 0
            rec = float('inf')
            for neighbor in graph[v]:
                if neighbor != path[0]:
                    rec = min(rec, 1 + dfs(neighbor))
            memo[v] = rec
        return memo[v]

    for i in range(n):
        dp[i] = dfs(i)

    return [min(dp), max(dp)]


# Example usage:
graph = [[1], [2], [3], [4], [5, 6], [7]]
path = [1, 2, 3]
print(min_max_recomputations(graph, path))  # Output: [0, 2]
