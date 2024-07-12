python
def min_cost_to_beautiful(n, m, s, queries):
    # Possible beautiful patterns
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    k = len(patterns)
    
    # Precompute costs for each pattern
    cost = [[0] * (n + 1) for _ in range(k)]
    
    for i in range(k):
        pattern = patterns[i]
        for j in range(n):
            cost[i][j + 1] = cost[i][j] + (s[j] != pattern[j % 3])
    
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for i in range(k):
            current_cost = cost[i][r] - cost[i][l - 1]
            min_cost = min(min_cost, current_cost)
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
    index = 3
    for _ in range(m):
        l = int(data[index])
        r = int(data[index + 1])
        queries.append((l, r))
        index += 2
    
    results = min_cost_to_beautiful(n, m, s, queries)
    
    for result in results:
        print(result)

