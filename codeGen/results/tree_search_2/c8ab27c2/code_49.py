from collections import Counter

def shortest_common_subsequence(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    uncommon_chars_S = set(Counter(S).keys())
    uncommon_chars_T = set(Counter(T).keys())

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                continue
            elif S[i-1] == T[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return max(0, (m - len(uncommon_chars_S.intersection(T))) if uncommon_chars_S.issubset(set(T)) else 0)

S = input()
T = input()

print(shortest_common_subsequence(S, T))
