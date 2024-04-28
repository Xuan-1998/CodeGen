def max_common_substrings():
    N = int(input())
    str1 = input()
    str2 = input()

    dp = [[0]*(N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + (dp[i-1][j-1] if i > 0 and j > 0 else 0)
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[N][N]

print(max_common_substrings())
