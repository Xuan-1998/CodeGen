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
        l = int(data[index])
        r = int(data[index + 1])
        queries.append((l, r))
        index += 2
    
    # Generate the three patterns
    pattern1 = "abc" * ((n // 3) + 1)
    pattern2 = "bca" * ((n // 3) + 1)
    pattern3 = "cab" * ((n // 3) + 1)
    
    # Calculate prefix costs for each pattern
    cost1 = [0] * (n + 1)
    cost2 = [0] * (n + 1)
    cost3 = [0] * (n + 1)
    
    for i in range(n):
        cost1[i + 1] = cost1[i] + (s[i] != pattern1[i])
        cost2[i + 1] = cost2[i] + (s[i] != pattern2[i])
        cost3[i + 1] = cost3[i] + (s[i] != pattern3[i])
    
    # Process each query
    results = []
    for l, r in queries:
        cost_to_pattern1 = cost1[r] - cost1[l - 1]
        cost_to_pattern2 = cost2[r] - cost2[l - 1]
        cost_to_pattern3 = cost3[r] - cost3[l - 1]
        min_cost = min(cost_to_pattern1, cost_to_pattern2, cost_to_pattern3)
        results.append(min_cost)
    
    # Print results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

