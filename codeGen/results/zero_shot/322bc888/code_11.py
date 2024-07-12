python
def min_cost_to_beautiful_string(n, m, s, queries):
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    costs = [[0] * (n + 1) for _ in range(6)]
    
    # Precompute the cost arrays
    for i in range(n):
        for j in range(6):
            costs[j][i + 1] = costs[j][i] + (s[i] != patterns[j][i % 3])
    
    results = []
    for l, r in queries:
        l -= 1
        min_cost = float('inf')
        for j in range(6):
            cost = costs[j][r] - costs[j][l]
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
        l = int(data[2 + 2 * i + 1])
        r = int(data[2 + 2 * i + 2])
        queries.append((l, r))
    
    results = min_cost_to_beautiful_string(n, m, s, queries)
    for result in results:
        print(result)

