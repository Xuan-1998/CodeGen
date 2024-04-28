def shortest_common_subsequence_length():
    S = input().strip()
    T = input().strip()

    dp = [0] * (len(S) + 1)
    for i in range(1, len(S) + 1):
        if S[i-1] != T[i-1]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = min(dp[i-1], dp[i-1])

    return -1 if max(dp) == 0 else len(S) - max(dp)
