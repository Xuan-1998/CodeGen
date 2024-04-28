code
def lcs_length(S, T, i=0, j=0):
    if i == len(S) or j == len(T):
        return 0
    if dp[i][j]:
        return dp[i][j]
    
    if S[i] == T[j]:
        dp[i][j] = 1 + lcs_length(S, T, i+1, j+1)
    else:
        dp[i][j] = max(lcs_length(S, T, i+1, j), lcs_length(S, T, i, j+1))
    
    return dp[i][j]

dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

S, T = input().split()
length_S, length_T = len(S), len(T)

result = lcs_length(S, T)
print(-result if result == 0 else -1)
