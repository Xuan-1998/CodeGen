def find_max_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    last_occurrence = [[-1, -1] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + (dp[i - 1][j - 1] if str1[i - 1] == str2[j - 1] else 0)
                last_occurrence[i][j] = [i - 1, j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    max_length = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[j - 1]:
                length = i - last_occurrence[i][j][0]
                max_length = max(max_length, length)

    return max_length
