from collections import defaultdict, deque

def solve(n, m, edges, k, fixed_path):
    # Build the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    # Initialize dp and memo
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    memo = {}

    def dfs(i, j):
        if i == k:  # Base case: when we've reached the end of the fixed path
            return dp[i][j]

        if (i, j) not in memo:
            min_recomputation = float('inf')
            for p in fixed_path[i]:
                recomputation = dfs(i + 1, p)
                min_recomputation = min(min_recomputation, recomputation + 1)

            dp[i][j] = min_recomputation
            memo[(i, j)] = dp[i][j]

        return memo.get((i, j), -1)

    # Find the minimum and maximum number of times the shortest path needs to be recomputed
    min_recomputation = dfs(0, fixed_path[0])
    max_recomputation = dfs(0, fixed_path[0])

    for i in range(1, k + 1):
        min_recomputation = min(min_recomputation, dfs(i, fixed_path[i - 1]))
        max_recomputation = max(max_recomputation, dfs(i, fixed_path[i - 1]))

    return min_recomputation, max_recomputation

# Example usage
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
fixed_path = list(map(int, input().split()))

min_recomputation, max_recomputation = solve(n, m, edges, k, fixed_path)

print(min_recomputation, max_recomputation)
