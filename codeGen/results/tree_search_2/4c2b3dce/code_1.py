def can_contain_ab(s):
    n = len(s)
    dp = [False] * (n + 1)
    
    for i in range(n):
        if s[i:i+2] == 'AB':
            dp[i+2] = True
    
    return any(dp[i:i+2] and dp[j:j+2] for i in range(n-1) for j in range(i+1, n))
