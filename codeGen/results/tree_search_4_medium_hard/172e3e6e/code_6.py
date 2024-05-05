def count_good_subsequences(n, a):
    MOD = 10**9 + 7

    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1 if a[i]%i==0 else 0

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if a[j]%j==0:
                for k in range(j-1, i-1, -1):
                    if a[k]%k==0:
                        dp[i][j] = (dp[i][j] + dp[i][k-1]) % MOD
    return sum(dp[0][i] for i in range(n)) % MOD

n = int(input())
a = list(map(int, input().split()))
print(count_good_subsequences(n, a))
