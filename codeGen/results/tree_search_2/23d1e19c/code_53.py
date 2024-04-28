from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    path = list(map(int, input().split()))

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        if i == path[0]:
            dp[i][0] = 0
        for j in range(k + 1):
            for k in graph[i]:
                if k == path[j + 1]:
                    dp[k][j + 1] = min(dp[k][j + 1], dp[i][j] + 1)
                    dp[k][j + 1] = max(dp[k][j + 1], dp[i][j] + 1)

    print(min(dp[-1]), max(dp[-1]))

if __name__ == '__main__':
    solve()
