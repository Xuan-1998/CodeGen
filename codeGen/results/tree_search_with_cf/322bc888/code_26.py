def min_cost_to_beautiful_substring(n, m, s, queries):
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    pattern_costs = [[0] * (n + 1) for _ in range(6)]
    
    for i in range(6):
        pattern = patterns[i]
        for j in range(n):
            pattern_costs[i][j + 1] = pattern_costs[i][j] + (s[j] != pattern[j % 3])
    
    results = []
    for l, r in queries:
        l -= 1  # Convert to 0-based index
        min_cost = float('inf')
        for i in range(6):
            cost = pattern_costs[i][r] - pattern_costs[i][l]
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
queries = [(int(data[2*i + 3]), int(data[2*i + 4])) for i in range(m)]

# Get the results
results = min_cost_to_beautiful_substring(n, m, s, queries)

# Print the results
for result in results:
    print(result)

