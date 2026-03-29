def beautyContest():
    t, l, r = map(int, input().split())
    
    # Check edge cases
    if l < 2 or r > 5*10**6:
        return -1
    
    dp = {0: 0}  # Base case: f(0) = 0
    
    for n in range(l, r+1):
        dp[n] = float('inf')
        for m in range(n//2 + 1):  # Merge up to half of the groups
            if m not in dp:
                continue
            dp[n] = min(dp[n], dp[m] + dp[n-m-1])
    
    return sum(t[i] * (dp[i] - i) for i in range(l, r+1)) % 10**9 + 7

print(beautyContest())
