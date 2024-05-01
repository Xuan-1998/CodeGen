def common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    # Preprocess suffix arrays
    str1_suffix = sorted((str1[i:] for i in range(N)))
    str2_suffix = sorted((str2[i:] for i in range(N)))

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j]) if str1_suffix.index(str1[:i]) < str2_suffix.index(str2[:j]) else 0
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]

if __name__ == "__main__":
    str1 = input().strip()
    str2 = input().strip()
    print(common_substrings(str1, str2))
