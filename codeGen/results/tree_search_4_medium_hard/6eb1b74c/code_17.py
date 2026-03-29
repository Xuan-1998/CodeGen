import sys

def color_text(t, S):
    n = len(S)
    dp = [[-1] * (n + 1) for _ in range(len(t) + 1)]
    
    # Initialize dp array
    for i in range(1, len(t) + 1):
        for j in range(n + 1):
            dp[i][j] = -1
    
    min_steps = float('inf')
    used_strings = []
    
    for i in range(len(t), 0, -1):
        for s_idx, s in enumerate(S):
            if t[i - len(s):i].startswith(s):
                temp = [dp[k][s_idx] + 1 if k == i else dp[k][s_idx] for k in range(i)]
                for j in range(n + 1):
                    dp[i][j] = min(dp[i][j], temp[j])
    
    if dp[-1][-1] == -1:
        return -1
    
    m = dp[-1][-1]
    used_strings = []
    
    for i in range(len(t), 0, -1):
        for j in range(n + 1):
            if dp[i][j] != dp[i - 1][j]:
                used_strings.append((s_idx, i - len(s)))
                break
    
    return m
