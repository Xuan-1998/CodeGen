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
        r = int(data[index + 1])
        queries.append((l, r))
        index += 2
    
    patterns = [
        "abc" * (n // 3 + 1),
        "bca" * (n // 3 + 1),
        "cab" * (n // 3 + 1)
    ]
    
    # Precompute costs for each pattern
    cost1 = [0] * (n + 1)
    cost2 = [0] * (n + 1)
    cost3 = [0] * (n + 1)
    
    for i in range(n):
        cost1[i + 1] = cost1[i] + (s[i] != patterns[0][i])
        cost2[i + 1] = cost2[i] + (s[i] != patterns[1][i])
        cost3[i + 1] = cost3[i] + (s[i] != patterns[2][i])
    
    results = []
    for l, r in queries:
        cost_to_pattern1 = cost1[r] - cost1[l]
        cost_to_pattern2 = cost2[r] - cost2[l]
        cost_to_pattern3 = cost3[r] - cost3[l]
        min_cost = min(cost_to_pattern1, cost_to_pattern2, cost_to_pattern3)
        results.append(min_cost)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

