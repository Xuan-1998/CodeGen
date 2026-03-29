from itertools import permutations

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    s = data[2]
    
    queries = []
    for i in range(m):
        l = int(data[3 + 2 * i]) - 1
        r = int(data[4 + 2 * i]) - 1
        queries.append((l, r))
    
    patterns = [''.join(p) for p in permutations('abc')]
    
    # Initialize the cost array
    cost = [[0] * (n + 1) for _ in range(6)]
    
    # Precompute the cost for each pattern
    for p_idx, pattern in enumerate(patterns):
        for i in range(n):
            cost[p_idx][i + 1] = cost[p_idx][i] + (s[i] != pattern[i % 3])
    
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for p_idx in range(6):
            current_cost = cost[p_idx][r + 1] - cost[p_idx][l]
            min_cost = min(min_cost, current_cost)
        results.append(min_cost)
    
    # Output results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

