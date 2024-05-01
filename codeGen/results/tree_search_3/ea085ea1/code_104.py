def maxCommonSubstrings(str1, str2):
    N = len(str1)
    M = len(str2)

    if N != M:
        return 0

    dp = [[False] * (N + 1) for _ in range(N + 1)]

    count = 0

    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = True
                count += 1
            else:
                break

            if dp[i-1][j-1] and i > 0 and j > 0:
                dp[i][j] = True
                count += 1

    return count - 2


# Receive input from standard input
str1 = input()
str2 = input()

# Print the answer to standard output
print(maxCommonSubstrings(str1, str2))
