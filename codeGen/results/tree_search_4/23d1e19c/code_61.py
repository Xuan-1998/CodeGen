from collections import deque

def solve(graph, s, t, path):
    n, m = len(graph), len(graph[0])
    dp = [[float('inf'), float('-inf')] for _ in range(n)]

    q = deque([(s, 0, 0)])
    dp[s] = [0, 0]

    while q:
        u, min_count, max_count = q.popleft()
        for v, w in enumerate(graph[u]):
            if w and (v not in path or path.index(v) != len(path) - 1):
                new_min_count = min(min_count + 1, dp[v][0])
                new_max_count = max(max_count, dp[v][1] + 1)
                if dp[v][0] > new_min_count and dp[v][1] < new_max_count:
                    q.append((v, new_min_count, new_max_count))
                    dp[v] = [new_min_count, new_max_count]
    return (dp[t][0], dp[t][1])

# Example usage
graph = [[0, 1, 1, 0],
         [1, 0, 1, 1],
         [1, 1, 0, 1],
         [0, 1, 1, 0]]

s, t = 0, 2
path = [0, 1]

min_recomputations, max_recomputations = solve(graph, s, t, path)
print(min_recomputations, max_recomputations)

