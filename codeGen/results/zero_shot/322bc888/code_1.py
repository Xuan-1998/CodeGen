python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])
    s = data[2]
    queries = [(int(data[2 + 2 * i]), int(data[3 + 2 * i])) for i in range(m)]

    patterns = ["abc", "bca", "cab"]
    costs = [[0] * (n + 1) for _ in range(3)]

    for i in range(n):
        for j in range(3):
            costs[j][i + 1] = costs[j][i] + (s[i] != patterns[j][i % 3])

    results = []
    for l, r in queries:
        l -= 1
        min_cost = min(costs[j][r] - costs[j][l] for j in range(3))
        results.append(min_cost)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()

