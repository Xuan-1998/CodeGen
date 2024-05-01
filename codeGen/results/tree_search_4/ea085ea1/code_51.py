from collections import defaultdict

def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    memo = defaultdict(int)

    def dfs(i, j):
        if i == 0 or j == 0:
            return 0
        if memo[(i, j)] > 0:
            return memo[(i, j)]
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dfs(i - 1, j - 1) + (str1[i - 1] == str2[j - 1])
        else:
            dp[i][j] = 0
        memo[(i, j)] = dp[i][j]
        return dp[i][j]

    max_count = 0
    for i in range(N):
        for j in range(N):
            count = dfs(i, j)
            if count > max_count:
                max_count = count

    return max_count

if __name__ == "__main__":
    str1 = input().strip()
    str2 = input().strip()
    print(max_common_substrings(str1, str2))
