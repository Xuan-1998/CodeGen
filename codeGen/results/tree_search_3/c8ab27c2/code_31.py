from collections import defaultdict

def uncommonFromS(T):
    dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
    prev_chars = defaultdict(int)
    
    for i in range(1, len(S) + 1):
        for j in range(1, min(i + 1, len(T) + 1)):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                prev_chars[S[i - 1]] = j - 1
            else:
                if i > 0 and j > 0 and S[i - 1] != T[j - 1]:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                elif prev_chars[S[i - 1]] < j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return len(S) - dp[-1][-1]

S, T = input().split()
print(uncommonFromS(T))
