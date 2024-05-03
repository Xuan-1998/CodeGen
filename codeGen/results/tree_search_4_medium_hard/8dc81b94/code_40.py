def can_make_zero():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[False] * 2 for _ in range(n)]
    
    dp[0][arr[0] == 0] = True
    
    for i in range(1, n):
        dp[i][0] = (dp[i-1][0] and arr[i] == 0) or (dp[i-1][1] and arr[i] != 0)
        dp[i][1] = dp[i-1][0]
    
    return "YES" if dp[-1][0] else "NO"

print(can_make_zero())
