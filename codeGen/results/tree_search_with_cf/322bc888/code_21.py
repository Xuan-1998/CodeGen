python
def min_cost_to_beautiful_string(n, m, s, queries):
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    pattern_count = len(patterns)
    
    # Precompute the cost to transform each prefix of the string into each pattern
    costs = [[0] * (n + 1) for _ in range(pattern_count)]
    
    for i in range(pattern_count):
        pattern = patterns[i]
        for j in range(n):
            costs[i][j + 1] = costs[i][j] + (s[j] != pattern[j % 3])
    
    results = []
    for l, r in queries:
        l -= 1  # Convert to 0-based index
        min_cost = float('inf')
        for i in range(pattern_count):
            min_cost = min(min_cost, costs[i][r] - costs[i][l])
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

# Processing the queries
results = min_cost_to_beautiful_string(n, m, s, queries)

# Output the results
for result in results:
    print(result)

