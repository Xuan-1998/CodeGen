python
def main():
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
    
    patterns = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    
    # Precompute costs for each pattern
    cost = [[0] * (n + 1) for _ in range(6)]
    
    for idx, pattern in enumerate(patterns):
        for i in range(n):
            cost[idx][i + 1] = cost[idx][i] + (s[i] != pattern[i % 3])
    
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for idx in range(6):
            min_cost = min(min_cost, cost[idx][r] - cost[idx][l - 1])
        results.append(min_cost)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

