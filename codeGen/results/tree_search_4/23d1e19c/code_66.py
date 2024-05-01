import sys

def solve():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    path = list(map(int, input().split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for u, v in edges:
        if u in path:
            for i in range(len(path) - 1, -1, -1):
                if path[i] == v:
                    j = i
                    break
            dp[v][j] += 1

    min_recomputations = sys.maxsize
    max_recomputations = 0

    for i in range(n + 1):
        for j in path:
            min_recomputations = min(min_recomputations, dp[i][j])
            max_recomputations = max(max_recomputations, dp[i][j])

    print(min_recomputations, max_recomputations)

solve()
