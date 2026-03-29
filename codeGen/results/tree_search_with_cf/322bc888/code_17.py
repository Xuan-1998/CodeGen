def min_cost_to_beautiful_string(n, m, s, queries):
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    costs = {pattern: [0] * (n + 1) for pattern in patterns}
    
    # Precompute costs for each pattern
    for pattern in patterns:
        for i in range(n):
            costs[pattern][i + 1] = costs[pattern][i] + (s[i] != pattern[i % 3])
    
    results = []
    for l, r in queries:
        l -= 1  # Convert to 0-based index
        min_cost = float('inf')
        for pattern in patterns:
            min_cost = min(min_cost, costs[pattern][r] - costs[pattern][l])
        results.append(min_cost)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
s = data[2]
queries = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(m)]

# Get results
results = min_cost_to_beautiful_string(n, m, s, queries)

# Print results
for result in results:
    print(result)

