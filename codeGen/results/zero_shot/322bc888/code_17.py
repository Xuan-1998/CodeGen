python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])
    s = data[2]
    queries = [(int(data[2 + 2 * i]) - 1, int(data[2 + 2 * i + 1]) - 1) for i in range(m)]

    patterns = ["abc", "acb", "bac", "bca", "cab", "cba"]

    # Create cost arrays for each pattern
    cost = [[0] * (n + 1) for _ in range(6)]

    for i in range(6):
        pattern = patterns[i]
        for j in range(n):
            cost[i][j + 1] = cost[i][j] + (s[j] != pattern[j % 3])

    results = []
    for l, r in queries:
        min_cost = float('inf')
        for i in range(6):
            min_cost = min(min_cost, cost[i][r + 1] - cost[i][l])
        results.append(min_cost)

    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()

