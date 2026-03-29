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
        queries.append((l_i, r_i))
    
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    cost_arrays = []
    
    for pattern in patterns:
        cost = [0] * (n + 1)
        for i in range(n):
            cost[i + 1] = cost[i] + (s[i] != pattern[i % 3])
        cost_arrays.append(cost)
    
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for cost in cost_arrays:
            min_cost = min(min_cost, cost[r] - cost[l - 1])
        results.append(min_cost)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

