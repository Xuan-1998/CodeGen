code
while True:
    try:
        n, k = map(int, input().split())
        s = input()
        
        dp = [[0]*(k+1) for _ in range(n+1)]
        
        # Edge cases
        if i < k:
            dp[i][j] = 0 if j < k else min(dp[0][0], dp[i-1][k-1]) + (s[j] != s[k-j])
        # Corner case
        elif j+k-1 > n:
            dp[i][j] = -1
        
        # Main loop
        for i in range(1, n+1):
            for j in range(max(0, k), min(n-k+2, n)):
                if s[j-k+1:j+1] not in "RGBRGBRGB...":
                    dp[i][j] = min(dp[max(0, i-1)][max(0, j-2)], dp[i-1][min(n-1, j+1)] + (s[j] != s[i-j]))
        
        print(min(dp[n-1]))
    except:
        break
