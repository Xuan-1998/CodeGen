===BEGIN CODE===
from collections import defaultdict
def uncommonFromS(S, T):
    dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
    last_t_index = defaultdict(int)
    
    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                last_t_index[S[i - 1]] = i - 1
            else:
                dp[i][j] = 0 if j > 1 and S[i - 1] == T[j - 2] else i
    
    result = float('inf')
    for i in range(len(S)):
        if S[i] not in last_t_index or i <= last_t_index[S[i]]:
            result = min(result, i + 1)
    
    return result if result != float('inf') else -1

S = input().strip()
T = input().strip()
print(uncommonFromS(S, T))
===END CODE===
