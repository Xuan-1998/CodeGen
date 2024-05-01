import sys

def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    path = list(map(int, input().split()))

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        if i == path[0]:
            dp[i][0] = 0
        else:
            dp[i][0] = sys.maxsize

    for j in range(1, k + 1):
        dp[path[j]][j] = 0

    for j in range(k - 1, -1, -1):
        for i in range(path[j], n + 1):
            if i == path[j]:
                continue
            if i < path[j]:
                dp[i][j] = min(dp[i][j], dp[path[j]][j] + 1)
            else:
                dp[i][j] = max(dp[i][j], dp[path[j]][j] + 1)

    print(min(max(dp[n][k - 1]), k))
