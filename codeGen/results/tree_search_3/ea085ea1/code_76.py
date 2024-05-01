import sys

def find_common_substr_count():
    str1 = input().strip()
    str2 = input().strip()

    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        count = 0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                i += 1
                j += 1
                count += 1
            else:
                break
        
        memo[(i, j)] = count
        return count

    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = dfs(i - 1, j - 1)

    return max(max(row) for row in dp) - 1

print(find_common_substr_count())
