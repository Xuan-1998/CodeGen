python
def min_cost_to_beautiful(s, l, r):
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    n = len(s)
    m = len(patterns)
    
    # Precompute the cost to transform every position to each pattern
    cost = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            cost[i][j] = (s[i] != patterns[j][i % 3])
    
    # Cumulative cost arrays
    cum_cost = [[0] * (n + 1) for _ in range(m)]
    for j in range(m):
        for i in range(1, n + 1):
            cum_cost[j][i] = cum_cost[j][i - 1] + cost[i - 1][j]
    
    # Answer the queries
    results = []
    for start, end in zip(l, r):
        start -= 1
        end -= 1
        min_cost = float('inf')
        for j in range(m):
            min_cost = min(min_cost, cum_cost[j][end + 1] - cum_cost[j][start])
        results.append(min_cost)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
s = data[2]

queries = []
for i in range(m):
    l_i = int(data[3 + 2 * i])
    r_i = int(data[4 + 2 * i])
    queries.append((l_i, r_i))

# Solving the problem
results = min_cost_to_beautiful(s, [q[0] for q in queries], [q[1] for q in queries])

# Output the results
for result in results:
    print(result)

