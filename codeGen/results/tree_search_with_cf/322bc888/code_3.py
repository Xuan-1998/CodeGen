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
        l = int(data[3 + 2 * i])
        r = int(data[4 + 2 * i])
        queries.append((l, r))
    
    # Patterns to compare against
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    
    # Initialize cost arrays
    cost = [[0] * (n + 1) for _ in range(6)]
    
    # Populate cost arrays
    for i in range(6):
        pattern = patterns[i]
        for j in range(n):
            cost[i][j + 1] = cost[i][j] + (s[j] != pattern[j % 3])
    
    # Process each query
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for i in range(6):
            current_cost = cost[i][r] - cost[i][l - 1]
            if current_cost < min_cost:
                min_cost = current_cost
        results.append(min_cost)
    
    # Print results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

