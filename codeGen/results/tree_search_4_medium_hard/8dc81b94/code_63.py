def zero_or_not():
    n = int(input())
    array = list(map(int, input().split()))
    
    dp = [[False for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = True
    
    for i in range(1, n+1):
        for j in range(i+1):
            if array[j-1] > 0:
                decrement_from_start = dp[j][i-j]
                decrement_from_end = dp[i][j]
                if (decrement_from_start and array[j-1] == 1) or decrement_from_end:
                    dp[i][j] = True
    
    print("YES" if dp[n][n] else "NO")

zero_or_not()
