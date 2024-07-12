python
def min_cost_to_beautiful(n, m, s, queries):
    # Generate all possible beautiful strings of length 3
    from itertools import permutations
    beautiful_patterns = [''.join(p) for p in permutations('abc', 3)]
    
    # Extend the patterns to cover lengths up to 6 (since we need to compare substrings up to length 6)
    extended_patterns = []
    for pattern in beautiful_patterns:
        for i in range(6):
            extended_patterns.append((pattern * (i // 3 + 1))[:i + 1])
    
    # Precompute the cost of transforming any substring to each beautiful pattern
    def compute_cost(sub, pattern):
        return sum(1 for a, b in zip(sub, pattern) if a != b)
    
    # Precompute costs for all substrings of length up to 6
    precomputed_costs = {}
    for length in range(1, 7):
        for i in range(n - length + 1):
            sub = s[i:i + length]
            costs = []
            for pattern in extended_patterns:
                if len(pattern) == length:
                    costs.append(compute_cost(sub, pattern))
            precomputed_costs[(i, i + length - 1)] = min(costs)
    
    # Process each query
    results = []
    for l, r in queries:
        l -= 1
        r -= 1
        length = r - l + 1
        if length <= 6:
            results.append(precomputed_costs[(l, r)])
        else:
            # For lengths greater than 6, we need to consider the repeating pattern
            min_cost = float('inf')
            for pattern in beautiful_patterns:
                full_pattern = (pattern * (length // 3 + 1))[:length]
                cost = compute_cost(s[l:r + 1], full_pattern)
                min_cost = min(min_cost, cost)
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
index = 3
for _ in range(m):
    l = int(data[index])
    r = int(data[index + 1])
    queries.append((l, r))
    index += 2

# Get results
results = min_cost_to_beautiful(n, m, s, queries)

# Output results
for result in results:
    print(result)

