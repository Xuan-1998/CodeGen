def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    s = data[2]
    queries = [(int(data[i]), int(data[i+1])) for i in range(3, len(data), 2)]
    
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    prefix_costs = [[0] * (n + 1) for _ in range(6)]
    
    for i, pattern in enumerate(patterns):
        for j in range(n):
            prefix_costs[i][j + 1] = prefix_costs[i][j] + (s[j] != pattern[j % 3])
    
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for i in range(6):
            cost = prefix_costs[i][r] - prefix_costs[i][l - 1]
            min_cost = min(min_cost, cost)
        results.append(min_cost)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()

