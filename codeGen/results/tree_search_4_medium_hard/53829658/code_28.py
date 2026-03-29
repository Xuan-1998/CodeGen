import sys

def dfs(parent, dp, i):
    if dp[i] != -1: return dp[i]
    min_dist = float('inf')
    for j in parent[i]:
        dist = dfs(parent, dp, j) + 1
        min_dist = min(min_dist, dist)
    dp[i] = min_dist
    return min_dist

def solve():
    n = int(sys.stdin.readline())
    parent = [[] for _ in range(n+1)]
    dp = [-1] * (n+1)

    # Read input and construct parent array
    for i in range(1, n):
        a, b = map(int, sys.stdin.readline().split())
        parent[b].append(a)

    # Calculate shortest distances using DFS
    capital = 0
    for i in range(1, n+1):
        dfs(parent, dp, i)
        if dp[i] < dp[capital]:
            capital = i

    # Print minimum number of roads to be inverted
    min_inverted = 0
    for i in range(1, n+1):
        min_inverted += max(dp[i]-dp[capital], 0)

    print(min_inverted)
    print(capital+1, end='')

if __name__ == "__main__":
    solve()
