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
    
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    costs = [[0] * (n + 1) for _ in range(6)]
    
    for i in range(6):
        pattern = patterns[i]
        for j in range(n):
            costs[i][j + 1] = costs[i][j] + (s[j] != pattern[j % 3])
    
    result = []
    for l, r in queries:
        min_cost = float('inf')
        for i in range(6):
            cost = costs[i][r] - costs[i][l - 1]
            min_cost = min(min_cost, cost)
        result.append(min_cost)
    
    for res in result:
        print(res)

if __name__ == "__main__":
    main()

