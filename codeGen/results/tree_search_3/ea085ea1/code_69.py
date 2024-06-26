def solve(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    max_count = 0

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_count = max(max_count, dp[i][j])

    return max_count

str1 = input()
str2 = input()

print(solve(str1, str2))
