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
    
    # Precompute the three beautiful patterns
    patterns = ["abc", "bca", "cab"]
    
    # Initialize cost arrays
    cost1 = [0] * (n + 1)
    cost2 = [0] * (n + 1)
    cost3 = [0] * (n + 1)
    
    # Precompute the costs
    for i in range(n):
        if s[i] != patterns[0][i % 3]:
            cost1[i + 1] = cost1[i] + 1
        else:
            cost1[i + 1] = cost1[i]
        
        if s[i] != patterns[1][i % 3]:
            cost2[i + 1] = cost2[i] + 1
        else:
            cost2[i + 1] = cost2[i]
        
        if s[i] != patterns[2][i % 3]:
            cost3[i + 1] = cost3[i] + 1
        else:
            cost3[i + 1] = cost3[i]
    
    # Answer each query using the precomputed costs
    results = []
    for l, r in queries:
        min_cost = min(
            cost1[r] - cost1[l - 1],
            cost2[r] - cost2[l - 1],
            cost3[r] - cost3[l - 1]
        )
        results.append(min_cost)
    
    # Print the results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

