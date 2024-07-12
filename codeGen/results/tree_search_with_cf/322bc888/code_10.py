python
def min_cost_to_beautiful(n, m, s, queries):
    # Define the beautiful patterns
    beautiful_patterns = [
        "abc", "acb", "bac", "bca", "cab", "cba"
    ]
    
    # Precompute the cost for each position to match each pattern
    cost = [[0] * n for _ in range(6)]
    
    for i, pattern in enumerate(beautiful_patterns):
        for j in range(n):
            cost[i][j] = (s[j] != pattern[j % 3])
    
    # Precompute prefix sums for each pattern's cost
    prefix_sum = [[0] * (n + 1) for _ in range(6)]
    
    for i in range(6):
        for j in range(1, n + 1):
            prefix_sum[i][j] = prefix_sum[i][j - 1] + cost[i][j - 1]
    
    results = []
    
    # Process each query
    for l, r in queries:
        l -= 1  # Convert to 0-based index
        min_cost = float('inf')
        for i in range(6):
            current_cost = prefix_sum[i][r] - prefix_sum[i][l]
            min_cost = min(min_cost, current_cost)
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
    l = int(data[2 + 2 * i + 1])
    r = int(data[2 + 2 * i + 2])
    queries.append((l, r))

# Get results
results = min_cost_to_beautiful(n, m, s, queries)

# Print results
for result in results:
    print(result)

