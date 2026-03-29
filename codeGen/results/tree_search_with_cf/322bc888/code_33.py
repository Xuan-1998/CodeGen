def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    s = data[2]
    queries = []
    for i in range(m):
        l = int(data[3 + 2 * i]) - 1
        r = int(data[4 + 2 * i])
        queries.append((l, r))
    
    patterns = [
        'abc', 'acb', 'bac', 'bca', 'cab', 'cba'
    ]
    
    # Precompute the cost arrays
    cost = [[0] * (n + 1) for _ in range(6)]
    
    for p in range(6):
        pattern = patterns[p]
        for i in range(1, n + 1):
            cost[p][i] = cost[p][i - 1]
            if s[i - 1] != pattern[(i - 1) % 3]:
                cost[p][i] += 1
    
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for p in range(6):
            min_cost = min(min_cost, cost[p][r] - cost[p][l])
        results.append(min_cost)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

