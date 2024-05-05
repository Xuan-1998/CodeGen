def max_or_value():
    n = int(input())
    s = input()
    
    dp = [0] * (n + 1)
    max_or = 0
    
    for i in range(1, n + 1):
        if s[i - 1] == '1':
            dp[i] = max(dp[i - 1], (dp[i - 1] | (1 << (i % 31))))
            max_or = max(max_or, dp[i])
    
    print(bin(max_or)[2:].zfill(n).lstrip('0'))
