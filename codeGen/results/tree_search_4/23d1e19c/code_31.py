def min_max_recompute_path():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    path = list(map(int, input().split()))

    dp = [[0, 0] for _ in range(k + 1)]

    for i in range(1, k + 1):
        if path[i - 1] == path[-1]:
            dp[i] = [dp[i - 1][0] + 1, min(dp[i - 1][0], dp[i - 1][1])]
        else:
            dp[i] = [min(dp[0][0], dp[i - 1][0]) + 1, max(dp[0][1], dp[i - 1][1])]

    print(*dp[-1])

if __name__ == "__main__":
    min_max_recompute_path()
