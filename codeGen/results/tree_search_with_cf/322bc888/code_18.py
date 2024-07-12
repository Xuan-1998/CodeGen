    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    costs = []

    # Precompute costs for each pattern
    for pattern in patterns:
        cost = [0] * (n + 1)
        for i in range(n):
            cost[i + 1] = cost[i] + (s[i] != pattern[i % 3])
        costs.append(cost)

    results = []
    for l, r in queries:
        l -= 1  # Convert to 0-based index
        min_cost = min(cost[r] - cost[l] for cost in costs)
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
index = 3
for _ in range(m):
    l = int(data[index])
    r = int(data[index + 1])
    queries.append((l, r))
    index += 2

# Get the results
results = min_cost_to_beautiful(n, m, s, queries)

# Print the results
for result in results:
    print(result)

