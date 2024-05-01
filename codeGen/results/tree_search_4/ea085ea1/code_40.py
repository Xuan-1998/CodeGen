from collections import defaultdict

def find_max_common_substrings(str1, str2):
    N = len(str1)
    M = len(str2)

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    max_common_substrings = 0

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if str1[i - 1] == str2[j - 1]:
                while i > 0 and j > 0 and str1[i - 1] == str2[j - 1]:
                    i -= 1
                    j -= 1

                max_common_substrings = max(max_common_substrings, dp[i][j])

    return max_common_substrings

if __name__ == "__main__":
    str1 = input().strip()
    str2 = input().strip()

    print(find_max_common_substrings(str1, str2))
