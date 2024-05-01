from collections import defaultdict

def find_max_common_substrings():
    N = int(input())
    str1, str2 = input().split()

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    memo_dict = defaultdict(int)

    def dfs(i, j):
        if i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                return dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                return max(dp[i - 1][j], dp[i][j - 1])
        else:
            return 0

    for i in range(N, -1, -1):
        for j in range(N, -1, -1):
            dp[i][j] = dfs(i, j)
            memo_dict[(i, j)] = dp[i][j]

    print(memo_dict.get((N, N), 0))

find_max_common_substrings()
