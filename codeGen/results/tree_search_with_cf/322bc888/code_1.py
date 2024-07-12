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
        queries.append((l - 1, r - 1))  # Convert to 0-based indexing
    
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    costs = [[0] * n for _ in range(6)]
    
    for i in range(6):
        pattern = patterns[i]
        for j in range(n):
            costs[i][j] = (s[j] != pattern[j % 3])
    
    prefix_sums = [[0] * (n + 1) for _ in range(6)]
    
    for i in range(6):
        for j in range(n):
            prefix_sums[i][j + 1] = prefix_sums[i][j] + costs[i][j]
    
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for i in range(6):
            cost = prefix_sums[i][r + 1] - prefix_sums[i][l]
            min_cost = min(min_cost, cost)
        results.append(min_cost)
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()

