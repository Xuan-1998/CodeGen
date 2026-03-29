def max_beauty(n, m, arr, bad_primes):
    dp = [[[[-1 for _ in range(2)] for _ in range(m+1)] for _ in range(n+1)]]
    
    for i in range(n+1):
        for j in range(min(i+1, m)+1):
            if i == 0 and j == 0:
                dp[i][j][0][1] = 0
            elif i > 0 and (arr[i-1] not in bad_primes or arr[i-1] % 2 != 0):
                for f in range(2):
                    for g in range(2):
                        if f == 0:
                            dp[i][j][f][g] = max(dp[i-1][j][f][g], dp[i-1][j-1][f][not g])
                        else:
                            dp[i][j][f][g] = max(dp[i-1][j][f][g], 0 if not g and arr[i-1] in bad_primes else -1)
            elif j > 0:
                for f in range(2):
                    for g in range(2):
                        dp[i][j][f][g] = max(dp[i-1][j][f][g], dp[i][j-1][f][not g])
            
    return dp[n][m][0][1]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))
print(max_beauty(n, m, arr, bad_primes))
