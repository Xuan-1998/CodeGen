def min_squares(n, m):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 0 or j == 0:
            return 0

        ans = float('inf')
        for k in range(1, min(i, j) + 1):
            if i - k >= 0 and j - k >= 0:
                ans = min(ans, dp(i - k, j - k) + (i // k + j // k))

        memo[(i, j)] = ans
        return ans

    return dp(n, m)

n, m = map(int, input().split())
print(min_squares(n, m))
