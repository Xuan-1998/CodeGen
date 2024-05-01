import sys

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    k = int(input())
    path = list(map(int, input().split()))
    
    dp = [[sys.maxsize, -1] for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        v = path[i]
        for w in graph[v]:
            if dp[w][0] > dp[v][0] + 1:
                dp[w][0] = dp[v][0] + 1
                dp[w][1] = dp[v][1] + (1 if i > 0 and path[i - 1] != v else 0)
    print(dp[-1][1], end=' ')

    # To find the minimum, we can simply subtract dp[0][1] from dp[t][1]
    min_recomputations = dp[-1][1] - dp[0][1]

    # For maximum, we need to keep track of the maximum recomputations needed along the path
    max_recomputations = 0
    for i in range(k):
        v = path[i]
        w = path[i + 1] if i < k - 1 else -1
        if dp[w][0] > dp[v][0] + 1:
            max_recomputations = max(max_recomputations, dp[w][1])
    
    print(max_recomputations)

if __name__ == "__main__":
    solve()
