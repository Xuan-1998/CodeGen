import sys

def min_squares(n, m):
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == 0 or j == 0:
            return 1
        ans = float('inf')
        for k in range(1, min(i, j) + 1):
            ans = min(ans, dfs(max(0, i - k), max(0, j - k)) + (i // k + j // k))
        memo[(i, j)] = ans
        return ans

    return dfs(n, m)

n, m = map(int, input().split())
print(min_squares(n, m))
