def can_make_zero():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[False for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        if sum(arr[:i+1]) <= 0:
            dp[0][i] = True
        else:
            break
    
    for i in range(n-2, -1, -1):
        if sum(arr[i:]) <= 0:
            dp[i][n-1] = True
        else:
            break
        
    for length in range(3, n+1):
        for i in range(n-length+1):
            k = i + length//2
            if (dp[0][k] and sum(arr[k:]) <= 0) or any(dp[i][j] for j in range(k+1, n)):
                dp[i][n-1] = True
    
    return "YES" if dp[0][n-1] else "NO"

print(can_make_zero())
