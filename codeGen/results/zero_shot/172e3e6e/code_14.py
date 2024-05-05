def count_good_subsequences():
    n = int(input())
    a = [int(x) for x in input().split()]
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n):
        if a[i] % i == 0:
            dp[i] += dp[i - 1]
        for j in range(i):
            if a[j] % j == 0 and j < i:
                dp[i] += dp[j]

    print(dp[n] % (10**9 + 7))
