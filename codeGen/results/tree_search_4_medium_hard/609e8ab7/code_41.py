    ===BEGIN CODE===
    T = int(input())
    for _ in range(T):
        n = int(input())
        p = list(map(int, input().split()))
        l = [list(map(int, input().split())) for _ in range(n)]
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            if p[i - 1] == 0:
                continue
            j = p[i - 1]
            dp[i] = min(dp[j] + 1, abs(l[j][1] - l[i][0]) + (l[i][1] - l[i][0]))
        print(dp[1])
    ===END CODE===
