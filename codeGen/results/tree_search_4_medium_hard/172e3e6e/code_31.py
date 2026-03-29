def solve():
    n = int(input())
    a = [int(x) for x in input().split()]

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        good_subseqs = 1
        for j in range(i):
            if i % a[j] == 0:
                good_subseqs *= (i | a[j]%i == 0)
        dp[i] = good_subseqs * dp[i-1]

    print(dp[n] % (10**9 + 7))
