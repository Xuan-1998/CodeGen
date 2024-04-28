import sys

def min_squares(n, m):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 0 or j == 0:
            return 0

        s = min(i, j)
        res = 1
        for k in range(1, s+1):
            res += dp(max(0, i-k), max(0, j-k))
        memo[(i, j)] = res
        return res

    return dp(n, m)

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(min_squares(n, m))
