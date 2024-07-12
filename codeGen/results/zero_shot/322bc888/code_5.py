python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    s = data[2]
    
    queries = []
    for i in range(m):
        l = int(data[3 + 2*i])
        r = int(data[4 + 2*i])
        queries.append((l-1, r-1))
    
    patterns = ["abc", "bca", "cab"]
    costs = [[0] * n for _ in range(3)]
    
    for i in range(n):
        for j in range(3):
            costs[j][i] = (s[i] != patterns[j][i % 3])
    
    prefix_sums = [[0] * (n + 1) for _ in range(3)]
    
    for j in range(3):
        for i in range(n):
            prefix_sums[j][i + 1] = prefix_sums[j][i] + costs[j][i]
    
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for j in range(3):
            min_cost = min(min_cost, prefix_sums[j][r + 1] - prefix_sums[j][l])
        results.append(min_cost)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

