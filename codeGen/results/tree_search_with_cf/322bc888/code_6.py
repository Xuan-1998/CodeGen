def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    s = data[2]
    
    queries = []
    index = 3
    for _ in range(m):
        l = int(data[index]) - 1
        r = int(data[index + 1]) - 1
        queries.append((l, r))
        index += 2
    
    patterns = ["abc", "acb", "bac"]
    cost = [[0] * (n + 1) for _ in range(3)]
    
    for i in range(3):
        for j in range(n):
            cost[i][j + 1] = cost[i][j] + (s[j] != patterns[i][j % 3])
    
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for i in range(3):
            min_cost = min(min_cost, cost[i][r + 1] - cost[i][l])
        results.append(min_cost)
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()

