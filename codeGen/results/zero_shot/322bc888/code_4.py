python
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
    
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    costs = {pattern: [0] * (n + 1) for pattern in patterns}
    
    for pattern in patterns:
        for i in range(n):
            costs[pattern][i + 1] = costs[pattern][i] + (s[i] != pattern[i % 3])
    
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for pattern in patterns:
            min_cost = min(min_cost, costs[pattern][r + 1] - costs[pattern][l])
        results.append(min_cost)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

