python
def min_cost_to_beautiful_string(n, m, s, queries):
    patterns = [
        "abc", "acb", "bac", "bca", "cab", "cba"
    ]
    
    # Create the 6 possible beautiful patterns for the given length
    beautiful_patterns = []
    for pattern in patterns:
        beautiful_patterns.append((pattern * ((n // 3) + 1))[:n])
    
    # Precompute the cost to transform each position to each pattern
    cost = [[0] * n for _ in range(6)]
    for i in range(6):
        for j in range(n):
            if s[j] != beautiful_patterns[i][j]:
                cost[i][j] = 1
    
    # Precompute prefix sums for the cost arrays
    prefix_cost = [[0] * (n + 1) for _ in range(6)]
    for i in range(6):
        for j in range(1, n + 1):
            prefix_cost[i][j] = prefix_cost[i][j - 1] + cost[i][j - 1]
    
    # Process each query
    results = []
    for l, r in queries:
        l -= 1
        min_cost = float('inf')
        for i in range(6):
            current_cost = prefix_cost[i][r] - prefix_cost[i][l]
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
queries = [(int(data[2 * i + 3]), int(data[2 * i + 4])) for i in range(m)]

# Get results
results = min_cost_to_beautiful_string(n, m, s, queries)

# Print results
for result in results:
    print(result)

