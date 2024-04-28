s = input().strip()
t = input().strip()

def longest_subsequence(s, t):
    m = len(s)
    n = len(t)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    max_length = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
    
    return m - max_length

print(longest_subsequence(s, t))
