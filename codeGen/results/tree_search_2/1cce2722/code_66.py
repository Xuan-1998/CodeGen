def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    prev_left = prev_right = float('-inf')
    
    for i in range(n):
        if a[i] == prev_left + 1:
            dp[i+1] = max(dp[i], dp[i-1])
        elif a[i] == prev_right - 1:
            dp[i+1] = max(dp[i], dp[i-1])
        else:
            dp[i+1] = dp[i]
        
        if i > 0:
            prev_left, prev_right = a[i-1], a[i]
    
    return n - dp[-1]

print(solve())
