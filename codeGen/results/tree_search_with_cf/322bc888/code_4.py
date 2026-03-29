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
    
    permutations = ["abc", "acb", "bac", "bca", "cab", "cba"]
    cost = [[0] * (n + 1) for _ in range(6)]
    
    for p_idx, perm in enumerate(permutations):
        for i in range(n):
            cost[p_idx][i + 1] = cost[p_idx][i] + (s[i] != perm[i % 3])
    
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for p_idx in range(6):
            current_cost = cost[p_idx][r + 1] - cost[p_idx][l]
            min_cost = min(min_cost, current_cost)
        results.append(min_cost)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

