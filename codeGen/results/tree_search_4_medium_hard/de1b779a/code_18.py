from functools import lru_cache

def max_profit():
    n, m, c0, d0 = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    @lru_cache(None)
    def dfs(i, j):
        if i < 0 or j < 0:
            return 0
        if i == n and j == m:
            return d0 - c0
        profit = max(dfs(i-1, j), dfs(i-1, j-1) + (d0 - c0) - min(c0, bi) for bi in map(int, input().split()))
        return max(profit, dfs(i-1, j-1) + di if i >= ci else 0)

    print(dfs(n, m))

if __name__ == "__main__":
    max_profit()
