S = input().strip()
T = input().strip()

def uncommon_subsequence_length(S, T):
    S_len, T_len = len(S), len(T)
    dp = [[0] * (T_len + 1) for _ in range(S_len + 1)]
    
    for i in range(1, S_len + 1):
        for j in range(1, T_len + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return S_len - dp[-1][-1]

print(uncommon_subsequence_length(S, T))
