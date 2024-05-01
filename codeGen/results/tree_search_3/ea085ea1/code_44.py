from collections import defaultdict

def max_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp = [[0] * (N + 1) for _ in range(N + 1)]

    # Base case: empty strings
    for i in range(N + 1):
        for j in range(N + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0

    # Fill up the memoization table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] != str2[j - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            else:
                # Check if the current substrings are equal
                for k in range(min(i, j), 0, -1):
                    if str1[:k] == str2[:k]:
                        dp[i][j] = max(dp[i][j], dp[k - 1][k - 1] + 1)
                        break

    print(dp[N][N])

max_common_substrings()
