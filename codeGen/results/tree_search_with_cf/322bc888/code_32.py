python
def min_cost_to_beautiful(n, m, s, queries):
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    k = 3  # Length of the patterns
    costs = [[0] * n for _ in range(6)]

    # Compute the cost to transform each position to each pattern
    for i in range(6):
        pattern = patterns[i]
        for j in range(n):
            costs[i][j] = (s[j] != pattern[j % k])
    
    # Compute prefix sums for each pattern
    prefix_sums = [[0] * (n + 1) for _ in range(6)]
    for i in range(6):
        for j in range(n):
            prefix_sums[i][j + 1] = prefix_sums[i][j] + costs[i][j]

    # Process each query
    results = []
    for (l, r) in queries:
        l -= 1  # Convert to 0-based index
        min_cost = float('inf')
        for i in range(6):
            cost = prefix_sums[i][r] - prefix_sums[i][l]
            min_cost = min(min_cost, cost)
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
index = 3
for i in range(m):
    l = int(data[index])
    r = int(data[index + 1])
    queries.append((l, r))
    index += 2

# Solve the problem
results = min_cost_to_beautiful(n, m, s, queries)

# Output the results
for result in results:
    print(result)

