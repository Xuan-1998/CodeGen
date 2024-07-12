python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    s = data[2]
    queries = [(int(data[2 + 2 * i]) - 1, int(data[2 + 2 * i + 1]) - 1) for i in range(m)]
    
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    costs = [[0] * n for _ in range(6)]
    
    for i in range(6):
        for j in range(n):
            costs[i][j] = (0 if s[j] == patterns[i][j % 3] else 1)
    
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
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()

