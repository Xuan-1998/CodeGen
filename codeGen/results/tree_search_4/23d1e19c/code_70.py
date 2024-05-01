import sys

def read_input():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    s, t = map(int, input().split())
    k = int(input())
    path = list(map(int, input().split()))
    return n, m, edges, s, t, k, path

def solve(n, m, edges, s, t, k, path):
    dp = [[0, 0] for _ in range(n)]
    for i in range(k):
        v = path[i]
        if dp[v][0] == 0:
            dp[v][0] = 1
            for j in range(1, n+1):
                dp[v][j] = sys.maxsize
        for j in range(min(i+1, k), -1, -1):
            u = path[j-1]
            if edges.count((u, v)) > 0:
                for x in range(n):
                    if edges.count((x, v)) > 0 and dp[x][i-j] == [1, j]:
                        dp[v][min(i+1, k)].[0] = min(dp[v][min(i+1, k)].[0], dp[u][i-j].0 + (dp[u][i-j].0 > 0))
                        dp[v][min(i+1, k)].[1] = max(dp[v][min(i+1, k)].[1], dp[u][i-j].1)
    return min(dp[t-1]), max(dp[t-1])

if __name__ == "__main__":
    n, m, edges, s, t, k, path = read_input()
    print(*solve(n, m, edges, s, t, k, path))
