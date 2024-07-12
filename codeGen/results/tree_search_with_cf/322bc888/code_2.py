python
def min_cost_to_beautiful(n, m, s, queries):
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    pattern_length = 3

    # Precompute the cost arrays for each pattern
    cost = [[0] * (n + 1) for _ in range(6)]
    
    for p in range(6):
        pattern = patterns[p]
        for i in range(n):
            cost[p][i + 1] = cost[p][i] + (s[i] != pattern[i % pattern_length])
    
    results = []
    for l, r in queries:
        l -= 1  # Convert to 0-based index
        min_cost = float('inf')
        for p in range(6):
            min_cost = min(min_cost, cost[p][r] - cost[p][l])
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

