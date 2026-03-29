def good_subsequences():
    n = int(input())
    a = [int(x) for x in input().split()]

    dp = [[0] * (n+1) for _ in range(n+1)]
    bad_count = 0

    for i in range(1, n+1):
        if a[i-1] % i == 0:
            good_prefix = min(i, bad_count)
            dp[i][good_prefix] += 1
            bad_count = 0
        else:
            bad_count += 1

    result = sum(dp[i][j] for i in range(1, n+1) for j in range(n+1))
    print(result % (10**9 + 7))

good_subsequences()
