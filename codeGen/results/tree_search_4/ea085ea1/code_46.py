def common_substrings(str1, str2):
    N = len(str1)
    memo = [[0] * (N + 1) for _ in range(N + 1)]

    def dfs(i, j):
        if i == 0 and j == 0:
            return 0
        if memo[i][j]:
            return memo[i][j]
        
        k = min(i, j)
        while k >= 0 and str1[k] != str2[j - k]:
            k -= 1
        
        res = 0
        if i > k and j > k:
            res = 1 + dfs(i - 1, j - 1)
        
        memo[i][j] = res
        return res

    return dfs(N - 1, N - 1)

# Read input from stdin
str1 = input().strip()
str2 = input().strip()

print(common_substrings(str1, str2))
