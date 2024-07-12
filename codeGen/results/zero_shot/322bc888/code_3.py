python
def min_cost_to_beautiful_string(n, m, s, queries):
    # Possible beautiful patterns
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    
    # Precompute prefix sums for each pattern
    prefix_sums = [[0] * (n + 1) for _ in range(6)]
    
    for i in range(n):
        for p in range(6):
            prefix_sums[p][i + 1] = prefix_sums[p][i] + (s[i] != patterns[p][i % 3])
    
    # Process each query
    results = []
    for l, r in queries:
        l -= 1  # Convert to 0-based index
        min_cost = float('inf')
        for p in range(6):
            cost = prefix_sums[p][r] - prefix_sums[p][l]
            min_cost = min(min_cost, cost)
        results.append(min_cost)
    
    return results

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    s = data[2]
    
    queries = []
    for i in range(m):
        l = int(data[3 + 2 * i])
        r = int(data[4 + 2 * i])
        queries.append((l, r))
    
    results = min_cost_to_beautiful_string(n, m, s, queries)
    
    for result in results:
        print(result)

