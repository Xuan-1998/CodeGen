def good_subsequences(a, n):
    mod = 10**9 + 7
    dp = [0] * (n+1)
    dp[0] = 1
    
    for i in range(1, n+1):
        if a[i-1] % i == 0:  # Check if a[i-1] is divisible by its index i
            for j in range(i):
                if a[j] % (j+1) == 0:
                    dp[i] = (dp[i] + dp[j]) % mod
    
    return sum(dp) % mod

n, *a = map(int, input().split())
print(good_subsequences(a, n))
