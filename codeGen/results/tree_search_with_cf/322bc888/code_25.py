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
        queries.append((l - 1, r - 1))  # converting to 0-based index

    # Possible beautiful strings of length 3
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    
    # Initialize prefix sum arrays for each pattern
    prefix_sums = [[0] * (n + 1) for _ in range(6)]
    
    # Compute prefix sums
    for i in range(n):
        for p in range(6):
            # Cost to transform s[i] to the correct character in pattern[p]
            cost = 1 if s[i] != patterns[p][i % 3] else 0
            prefix_sums[p][i + 1] = prefix_sums[p][i] + cost
    
    # Process each query
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for p in range(6):
            cost = prefix_sums[p][r + 1] - prefix_sums[p][l]
            if cost < min_cost:
                min_cost = cost
        results.append(min_cost)
    
    # Print results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

