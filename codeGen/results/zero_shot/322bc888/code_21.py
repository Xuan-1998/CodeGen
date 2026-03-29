def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    s = data[2]
    queries = []
    for i in range(m):
        l = int(data[3 + 2*i])
        r = int(data[3 + 2*i + 1])
        queries.append((l, r))

    # Patterns
    patterns = ["abc", "acb", "bac"]
    
    # Precompute costs for each pattern
    costs = [[0] * (n + 1) for _ in range(3)]
    
    for i in range(n):
        for j in range(3):
            costs[j][i + 1] = costs[j][i] + (s[i] != patterns[j][i % 3])
    
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for j in range(3):
            min_cost = min(min_cost, costs[j][r] - costs[j][l - 1])
        results.append(min_cost)
    
    # Print the results for each query
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

