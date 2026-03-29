from collections import defaultdict

def max_profit(n, m, c0, d0):
    memo = defaultdict(int)

    def dp(i, j):
        if i == 0 and j > 0:
            return d0
        if i > 0 and j == 0:
            return c0
        if (i, j) in memo:
            return memo[(i, j)]

        if i > 0:
            profit1 = dp(i - c0, j - 1) + d0
            profit2 = dp(i, j - 1)
            memo[(i, j)] = max(profit1, profit2)

        else:
            memo[(i, j)] = dp(0, j - 1) + d0

        return memo[(i, j)]

    return dp(n, m)

if __name__ == "__main__":
    n, m, c0, d0 = map(int, input().split())
    print(max_profit(n, m, c0, d0))
