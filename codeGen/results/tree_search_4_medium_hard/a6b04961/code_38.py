import sys

def read_input():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, m, edges

def solve(n, m, edges):
    dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(n + 1)]

    # Base case: when there are no more edges to consider
    for i in range(1, n + 1):
        for j in range(0, m + 1):
            dp[i][j][i] = (n - i) * (m - j)

    # Fill up the dynamic programming table
    for i in range(2, n + 1):
        for j in range(m, 0, -1):
            for k in range(i, n + 1):
                # Calculate the maximum beauty that can be achieved by extending the current tail or starting a new spine
                extend = dp[i-1][j][k] + (n - i) * (m - j)
                start_new_spine = dp[0][j][k]
                dp[i][j][k] = max(extend, start_new_spine)

    return dp[n][0][n]

if __name__ == "__main__":
    n, m, edges = read_input()
    print(solve(n, m, edges))
