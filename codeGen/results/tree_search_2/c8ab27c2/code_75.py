def shortest_uncommon_subsequence():
    S, T = input().split()
    dp = [[-1] * (len(T) + 1) for _ in range(len(S) + 1)]
    
    for i in range(len(S)):
        for j in range(len(T)):
            if S[i] == T[j]:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = min(dp[i][j], dp[i+1][j])
    
    res = float('inf')
    for i in range(len(S)):
        if dp[i][-1] == -1:
            res = min(res, i + 1)
    
    print(-1 if res == float('inf') else len(S) - res)

shortest_uncommon_subsequence()
