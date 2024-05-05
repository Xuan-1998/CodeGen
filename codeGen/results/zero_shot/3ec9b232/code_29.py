def mergeArrays():
    n = int(input())
    m = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(n):
        if m[i] == i + 1:
            dp[i + 1] += dp[i]
        elif m[i] > i + 1:
            if i >= 2 and m[i] - (i - 1) >= i + 1:
                dp[i + 1] = (dp[i - 2] + dp[i]) % (10**9 + 7)
            else:
                dp[i + 1] += dp[i]
    
    print(dp[n] % (10**9 + 7))
