def findUncommonSubsequence():
    S, T = input().split(), input().split()
    
    # Initialize a 2D dictionary for memoization
    dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i-1] == T[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            elif dp[i-1][j] > 0 or dp[i][j-1] > 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = min(i, j)

    # Calculate the length of the shortest uncommon subsequence
    uncommon_subseq_len = len(S) - dp[-1][-1]

    print(uncommon_subseq_len)
