def min_cost_to_beautiful(s, l, r, patterns):
    min_cost = float('inf')
    for pattern in patterns:
        cost = 0
        for i in range(l, r + 1):
            if s[i] != pattern[(i - l) % 3]:
                cost += 1
        min_cost = min(min_cost, cost)
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
        l = int(data[index]) - 1
        r = int(data[index + 1]) - 1
        queries.append((l, r))
        index += 2
    
    patterns = [
        "abc", "acb", "bac", "bca", "cab", "cba"
    ]
    
    results = []
    for l, r in queries:
        results.append(min_cost_to_beautiful(s, l, r, patterns))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

