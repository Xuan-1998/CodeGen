def max_common_substrings(str1, str2):
    N = len(str1)
    DP = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        for j in range(N + 1):
            if i == 0 or j == 0:
                DP[i][j] = 1
            elif str1[i-1] == str2[j-1]:
                DP[i][j] = 1 + DP[i-1][j-1]
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1]) + 1

    return DP[N-1][N-1]

# Example usage
str1 = input().strip()
str2 = input().strip()

print(max_common_substrings(str1, str2))
