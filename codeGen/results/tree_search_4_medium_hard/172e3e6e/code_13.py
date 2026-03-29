def count_good_subsequences():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        for k in range(i):
            if a[i - 1] % k == 0:
                dp[i][k] = dp[k-1][k-1] if k > 0 else 1
            else:
                dp[i][k] = 0

    total = 0
    for i in range(n + 1):
        total += dp[n][i]
    print(total % (10**9 + 7))
