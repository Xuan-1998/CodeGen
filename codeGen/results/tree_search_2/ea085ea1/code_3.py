def max_common_substrings(str1, str2):
    N = len(str1)
    DP = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[j - 1]:
                DP[i][j] = DP[i - 1][j - 1] + 1
            else:
                DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

    return DP[N][N]

str1, str2 = input().split()
print(max_common_substrings(str1, str2))
