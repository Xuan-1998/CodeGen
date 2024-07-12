python
def min_operations_to_beautiful(n, m, s, queries):
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    pattern_costs = [[0] * (n + 1) for _ in range(6)]

    # Precompute the cost for each position and each pattern
    for i in range(n):
        for j in range(6):
            pattern_costs[j][i + 1] = pattern_costs[j][i] + (s[i] != patterns[j][i % 3])

    results = []
    for l, r in queries:
        min_cost = float('inf')
        for j in range(6):
            cost = pattern_costs[j][r] - pattern_costs[j][l - 1]
            min_cost = min(min_cost, cost)
        results.append(min_cost)

    return results

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
s = data[2]
queries = []
for i in range(m):
    l = int(data[3 + 2 * i])
    r = int(data[4 + 2 * i])
    queries.append((l, r))

# Process and output results
results = min_operations_to_beautiful(n, m, s, queries)
for result in results:
    print(result)

