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
    
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    k = len(patterns)
    
    # Initialize cost arrays
    cost = [[0] * n for _ in range(k)]
    
    for i in range(k):
        pattern = patterns[i]
        for j in range(n):
            if j % 3 == 0:
                expected_char = pattern[0]
            elif j % 3 == 1:
                expected_char = pattern[1]
            else:
                expected_char = pattern[2]
            
            if s[j] != expected_char:
                cost[i][j] = 1
            
            if j > 0:
                cost[i][j] += cost[i][j-1]
    
    results = []
    for l, r in queries:
        l -= 1
        r -= 1
        min_cost = float('inf')
        for i in range(k):
            if l == 0:
                current_cost = cost[i][r]
            else:
                current_cost = cost[i][r] - cost[i][l-1]
            min_cost = min(min_cost, current_cost)
        results.append(min_cost)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

