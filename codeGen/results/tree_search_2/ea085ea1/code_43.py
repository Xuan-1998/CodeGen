def find_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    hashmap = {}

    max_count = 0

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                hashmap[(str1[:i], str2[:j])] = dp[i][j]
            else:
                if (str1[:i], str2[:j]) in hashmap:
                    dp[i][j] = hashmap[(str1[:i], str2[:j])]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            max_count = max(max_count, dp[i][j])

    print(max_count)

find_common_substrings()
