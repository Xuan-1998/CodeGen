=*=BEGIN CODE*="
def find_LCS(S, T):
    m = len(S)
    n = len(T)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


def find_shortest_uncommon_subsequence(S, T):
    m = len(S)
    n = len(T)

    lcs_length = find_LCS(S, T)
    uncommon_subsequence_length = max(m, n) - lcs_length

    return uncommon_subsequence_length


=*=END CODE*="
