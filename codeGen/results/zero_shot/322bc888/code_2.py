python
def min_operations_to_beautiful(n, m, s, queries):
    patterns = ["abc", "acb", "bac"]
    costs = [[0] * (n + 1) for _ in range(3)]
    
    for i in range(3):
        for j in range(n):
            costs[i][j + 1] = costs[i][j] + (s[j] != patterns[i][j % 3])
    
    results = []
    for l, r in queries:
        l -= 1
        min_cost = float('inf')
        for i in range(3):
            min_cost = min(min_cost, costs[i][r] - costs[i][l])
        results.append(min_cost)
    
    return results

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    s = data[2]
    queries = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(m)]
    
    results = min_operations_to_beautiful(n, m, s, queries)
    
    for result in results:
        print(result)

