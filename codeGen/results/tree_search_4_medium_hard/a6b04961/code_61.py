import sys

def read_input():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, m, edges

def solve(n, m, edges):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(m + 1):
        for j in range(i + 1):
            if i > 0:
                dp[i][j] = max(dp[max(0, i - 1)][k] for k in range(j + 1)) * (i * (j + 1))
            else:
                dp[i][j] = 1
    return dp[n][m]

if __name__ == "__main__":
    n, m, edges = read_input()
    print(solve(n, m, edges))
