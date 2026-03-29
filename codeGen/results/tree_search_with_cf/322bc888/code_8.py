def main():
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
        queries.append((l_i - 1, r_i - 1))  # Convert to zero-based index
    
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    k = len(patterns)
    
    # Precompute prefix costs for each pattern
    prefix_cost = [[0] * (n + 1) for _ in range(k)]
    
    for p in range(k):
        pattern = patterns[p]
        for i in range(n):
            prefix_cost[p][i + 1] = prefix_cost[p][i] + (s[i] != pattern[i % 3])
    
    # Answer each query
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for p in range(k):
            cost = prefix_cost[p][r + 1] - prefix_cost[p][l]
            min_cost = min(min_cost, cost)
        results.append(min_cost)
    
    # Print results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

