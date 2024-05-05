def goodSubsequences():
    n = int(input())
    a = [int(x) for x in input().split()]
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, min(i+1, n)+1):
            if j > 0 and a[i-1]%j == 0:
                dp[i][j] = (dp[i-1][j-1] or (a[i-1]//j == 0)) and (i > 1)
            else:
                dp[i][j] = dp[i-1][min(j, i)]
    
    return sum(dp[n][i] for i in range(1, n+1)) % (10**9 + 7)

print(goodSubsequences())
