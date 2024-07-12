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
        l_i = int(data[3 + 2 * i])
        r_i = int(data[4 + 2 * i])
        queries.append((l_i, r_i))

    # Generate the 6 possible "beautiful" strings
    beautiful_patterns = [
        "abc", "acb", "bac", "bca", "cab", "cba"
    ]
    
    # Initialize the dp array
    dp = [[0] * (n + 1) for _ in range(6)]
    
    # Compute the dp array
    for k in range(6):
        pattern = beautiful_patterns[k]
        for i in range(1, n + 1):
            dp[k][i] = dp[k][i - 1] + (s[i - 1] != pattern[(i - 1) % 3])
    
    # Answer the queries
    results = []
    for l_i, r_i in queries:
        min_cost = float('inf')
        for k in range(6):
            cost = dp[k][r_i] - dp[k][l_i - 1]
            if cost < min_cost:
                min_cost = cost
        results.append(min_cost)
    
    # Print the results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

