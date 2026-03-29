def beautifulGirls():
    t, l, r = map(int, input().split())
    
    dp = [0] * (r + 1)
    dp[2] = 1
    
    for i in range(3, r + 1):
        dp[i] = dp[i - 1] + 1
    
    result = 0
    for i in range(l, r + 1):
        result += t * (dp[i] - dp[i - 1])
    
    return str(result % (10**9 + 7))

print(beautifulGirls())
