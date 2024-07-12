def min_cost_to_beautiful_string(n, m, s, queries):
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    
    # Create prefix sum arrays for each pattern
    prefix_costs = [[0] * (n + 1) for _ in range(6)]
    
    for i in range(6):
        pattern = patterns[i]
        for j in range(n):
            prefix_costs[i][j + 1] = prefix_costs[i][j] + (s[j] != pattern[j % 3])
    
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for i in range(6):
            cost = prefix_costs[i][r] - prefix_costs[i][l - 1]
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
    idx = 3
    for _ in range(m):
        l = int(data[idx])
        r = int(data[idx + 1])
        queries.append((l, r))
        idx += 2
    
    results = min_cost_to_beautiful_string(n, m, s, queries)
    for result in results:
        print(result)

