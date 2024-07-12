python
def min_cost_to_beautiful_string(n, m, s, queries):
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    k = len(patterns)

    # Precompute the cost to transform s[0:i+1] to each pattern
    costs = [[0] * (n + 1) for _ in range(k)]
    for i in range(n):
        for j in range(k):
            costs[j][i + 1] = costs[j][i] + (s[i] != patterns[j][i % 3])

    # Process each query
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for j in range(k):
            min_cost = min(min_cost, costs[j][r] - costs[j][l - 1])
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

# Get results
results = min_cost_to_beautiful_string(n, m, s, queries)

# Output results
for result in results:
    print(result)

