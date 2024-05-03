def can_make_zero():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[False] * 1000001 for _ in range(n+1)]
    dp[0][0] = True
    
    for i in range(1, n+1):
        for j in range(arr[i-1]+1):
            if dp[i-1][j]:
                dp[i][j+arr[i-1]-j] = True
    
    result = "YES" if any(dp[n][k] for k in range(n)) else "NO"
    print(result)

can_make_zero()
