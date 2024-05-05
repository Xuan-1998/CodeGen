def solution(b):
    n = len(b)
    max_val = max(b)
    dp = [[False] * (max_val + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        prev_val = b[i - 1]
        for j in range(max_val + 1):
            if prev_val <= j:
                dp[i][j] = or(dp[i][j], dp[i - 1][j - prev_val])
    
    return "YES" if any(dp[n]) else "NO"
