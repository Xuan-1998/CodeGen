python
def preprocess_costs(s, n):
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    costs = {pattern: [0] * (n + 1) for pattern in patterns}

    for pattern in patterns:
        pattern_len = len(pattern)
        for i in range(n):
            costs[pattern][i + 1] = costs[pattern][i] + (s[i] != pattern[i % pattern_len])
    
    return costs

def min_cost_to_beautify_substring(costs, l, r):
    min_cost = float('inf')
    for pattern in costs:
        min_cost = min(min_cost, costs[pattern][r] - costs[pattern][l - 1])
    return min_cost

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

    costs = preprocess_costs(s, n)
    
    results = []
    for l, r in queries:
        results.append(min_cost_to_beautify_substring(costs, l, r))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

