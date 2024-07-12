def min_operations_to_beautiful(n, m, s, queries):
    # Precompute all possible beautiful strings of length up to 3
    beautiful_patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    pattern_costs = []

    for pattern in beautiful_patterns:
        cost = [0] * (n + 1)
        for i in range(n):
            cost[i + 1] = cost[i] + (s[i] != pattern[i % 3])
        pattern_costs.append(cost)

    results = []
    for l, r in queries:
        min_cost = float('inf')
        for cost in pattern_costs:
            min_cost = min(min_cost, cost[r] - cost[l - 1])
        results.append(min_cost)

    return results

# Reading input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])
s = data[2]
queries = []
for i in range(m):
    l = int(data[3 + 2 * i])
    r = int(data[3 + 2 * i + 1])
    queries.append((l, r))

# Get results
results = min_operations_to_beautiful(n, m, s, queries)

# Print results
for result in results:
    print(result)

