def uncommon_from_s(s, t):
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] != t[j - 1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
            else:
                dp[i][j] = dp[i-1][j-1]
    
    result = 0
    for i in range(len(s), -1, -1):
        if any(c not in t for c in s[:i]):
            result = max(result, i)
            break
    
    return len(s) - result if result else -1

s = input().strip()
t = input().strip()

print(uncommon_from_s(s, t))
