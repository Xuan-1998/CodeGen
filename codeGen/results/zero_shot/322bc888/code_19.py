python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    s = data[2]
    queries = [(int(data[i*2+3])-1, int(data[i*2+4])-1) for i in range(m)]
    
    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]
    costs = [[0] * (n + 1) for _ in range(6)]
    
    for i in range(6):
        pattern = patterns[i]
        for j in range(n):
            costs[i][j+1] = costs[i][j] + (s[j] != pattern[j % 3])
    
    results = []
    for l, r in queries:
        min_cost = float('inf')
        for i in range(6):
            min_cost = min(min_cost, costs[i][r+1] - costs[i][l])
        results.append(min_cost)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

