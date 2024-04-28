S = input().strip()
T = input().strip()

def uncommon_subsequence_length(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    max_len = -1
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if i > j and dp[i][j] < (i - j):
                max_len = i - j
    return max_len

print(uncommon_subsequence_length(S, T))
