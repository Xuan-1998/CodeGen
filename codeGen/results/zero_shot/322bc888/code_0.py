def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    s = data[2]
    queries = [(int(data[2*i+3])-1, int(data[2*i+4])-1) for i in range(m)]
    
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    costs = [[0] * (n + 1) for _ in range(6)]
    
    for i in range(6):
        pattern = patterns[i]
        for j in range(n):
            costs[i][j + 1] = costs[i][j] + (s[j] != pattern[j % 3])
    
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for i in range(6):
            current_cost = costs[i][r + 1] - costs[i][l]
            min_cost = min(min_cost, current_cost)
        results.append(min_cost)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()

