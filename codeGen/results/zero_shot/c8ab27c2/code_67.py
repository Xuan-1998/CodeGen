S = input().strip()
T = input().strip()

def uncommon_subsequence_length(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                continue
            elif j == 0:
                dp[i][j] = i
            else:
                if S[i - 1] != T[j - 1]:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                else:
                    dp[i][j] = dp[i - 1][j - 1]
    
    return max(0, m - dp[m][n])

print(uncommon_subsequence_length(S, T))
