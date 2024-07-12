def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])
    s = data[2]
    queries = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(m)]

    # Generate the 6 repeating patterns
    patterns = [
        "abc", "acb", "bac", "bca", "cab", "cba"
    ]
    # Extend patterns to length n
    extended_patterns = []
    for pattern in patterns:
        extended_patterns.append((pattern * ((n // 3) + 1))[:n])

    # Precompute the cost to convert each character in s to match each pattern
    cost = [[0] * n for _ in range(6)]
    for i in range(6):
        for j in range(n):
            if s[j] != extended_patterns[i][j]:
                cost[i][j] = 1

    # Build prefix sum arrays for each pattern
    prefix_sums = [[0] * (n + 1) for _ in range(6)]
    for i in range(6):
        for j in range(1, n + 1):
            prefix_sums[i][j] = prefix_sums[i][j - 1] + cost[i][j - 1]

    # Process each query
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for i in range(6):
            current_cost = prefix_sums[i][r] - prefix_sums[i][l - 1]
            if current_cost < min_cost:
                min_cost = current_cost
        results.append(min_cost)

    # Print the results for each query
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

