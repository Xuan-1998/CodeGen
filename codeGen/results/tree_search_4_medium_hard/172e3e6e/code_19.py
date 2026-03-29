def count_good_subsequences():
    n = int(input())
    a = list(map(int, input().split()))
    
    MOD = 10**9 + 7
    
    dp = [[False] * (n+1) for _ in range(n+1)]
    good_subseqs = [0] * (n+1)
    
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a[i] % j == 0:
                dp[i][j] = dp[i-1][j-1] or True
                good_subseqs[j] += dp[i][j]
    
    return sum(good_subseqs) % MOD

print(count_good_subsequences())
