def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    s = data[2]
    
    queries = []
    for i in range(m):
        l = int(data[3 + 2 * i]) - 1  # convert to 0-indexed
        r = int(data[4 + 2 * i]) - 1  # convert to 0-indexed
        queries.append((l, r))
    
    # Possible beautiful patterns
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    k = len(patterns)
    
    # Precompute the cost to transform the original string to each beautiful pattern
    cost = [[0] * (n + 1) for _ in range(k)]
    
    for i in range(k):
        pattern = patterns[i]
        for j in range(n):
            cost[i][j + 1] = cost[i][j] + (s[j] != pattern[j % 3])
    
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for i in range(k):
            min_cost = min(min_cost, cost[i][r + 1] - cost[i][l])
        results.append(min_cost)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

