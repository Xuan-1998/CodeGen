import sys

def read_input():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, m, edges

def solve(n, m, edges):
    seen = set()
    g = {}
    for u, v in edges:
        if u not in g:
            g[u] = []
        if v not in g:
            g[v] = []
        g[u].append(v)
        g[v].append(u)

    dp = [[0, 0, 0] for _ in range(n + 1)]
    for i in range(2):
        dp[i][i] = [0, 0, 0]

    for i in range(1, n):
        for j in range(i):
            if j not in seen:
                seen.add(j)
                for k in range(i, j, -1):
                    new_dp = list(dp[k-1])
                    new_dp[2] += dp[j][k-1][0]
                    for l in range(k-1, j-1, -1):
                        if (l not in g or k not in g[l]) and (j+1 <= n):
                            new_dp[0] = max(new_dp[0], dp[l][k-1][2])
                            new_dp[1] += 1
                    for l in range(k-1, j-1, -1):
                        if (l not in g or k not in g[l]):
                            new_dp[2] += dp[l][k-1][0]
                    dp[j][i] = new_dp

    return max(dp[-1])

if __name__ == "__main__":
    n, m, edges = read_input()
    print(solve(n, m, edges))
