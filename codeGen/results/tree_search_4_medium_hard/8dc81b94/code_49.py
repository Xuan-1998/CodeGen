def can_make_zero():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[False] * (max(arr) + 1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = True
    
    for i in range(1, n+1):
        for k in range(max(arr)+1):
            if arr[i-1] > k:
                dp[i][k] = dp[i-1][0]
            else:
                dp[i][k] = max(dp[i-1][k], dp[min(i,k)][arr[i-1]-1])
    
    print("YES" if any(not state[-1] for state in dp) else "NO")
