python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    s = data[2]
    queries = [(int(data[3 + 2 * i]), int(data[3 + 2 * i + 1])) for i in range(m)]
    
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    pattern_costs = [[0] * (n + 1) for _ in range(6)]
    
    for p_idx, pattern in enumerate(patterns):
        for i in range(n):
            pattern_costs[p_idx][i + 1] = pattern_costs[p_idx][i] + (s[i] != pattern[i % 3])
    
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for p_idx in range(6):
            cost = pattern_costs[p_idx][r] - pattern_costs[p_idx][l - 1]
            if cost < min_cost:
                min_cost = cost
        results.append(min_cost)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

