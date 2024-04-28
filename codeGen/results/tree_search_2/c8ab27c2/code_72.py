def shortestUncommonSubsequence(S, T):
    dp = [[-1] * (len(T) + 1) for _ in range(len(S) + 1)]

    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i-1] == T[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][k] for k in range(j+1))

    result = -1
    for i in range(1, len(S) + 1):
        if dp[i][0] == -1:
            result = i

    return result if result != -1 else -1

S = input().strip()
T = input().strip()

print(shortestUncommonSubsequence(S, T))
