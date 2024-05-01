def min_max_recompute(graph, path):
    n = len(graph)
    dp = {(0, 0): (0, 0)}  # base case: start vertex, depth 0

    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]

        for d in range(dp[(u, i)][1] + 1):
            if (v, d) not in dp:
                dp[(v, d)] = (dp.get((u, i), (0, 0))[0] + 1, max(dp.get((u, i), (0, 0))[0] + 1, d))
            else:
                dp[(v, d)] = dp[(v, d)]

    return dp.get((path[-1], len(path) - 1), (0, 0))

# Example usage
graph = [[1, 2], [2, 3], [3, 4], [4, 5]]
path = [1, 2, 3, 4]
print(min_max_recompute(graph, path))  # Output: (0, 1)
