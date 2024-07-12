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
    
    patterns = [
        "abc", "acb", "bac"
    ]
    
    # Precompute the cost to transform s into each of the three patterns
    costs = [[0] * (n + 1) for _ in range(3)]
    
    for i in range(n):
        for p in range(3):
            costs[p][i + 1] = costs[p][i] + (s[i] != patterns[p][i % 3])
    
    # Process each query
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for p in range(3):
            cost = costs[p][r + 1] - costs[p][l]
            min_cost = min(min_cost, cost)
        results.append(min_cost)
    
    # Print the results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

