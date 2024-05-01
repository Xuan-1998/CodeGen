from collections import defaultdict

def uncommon_from_s_t(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row of the dp array
    for i in range(1, m + 1):
        if s[i - 1] != t[0]:
            dp[i][0] = dp[i - 1][0] + 1
        else:
            dp[i][0] = 1
    
    # Fill up the rest of the dp array based on whether characters match or not
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Find the first row where all characters have been matched, and return its length if it's shorter than m
    for i in range(m + 1):
        if all(k == n for k in dp[i]):
            return m - i
    
    return -1

s = input()
t = input()
print(uncommon_from_s_t(s, t))
