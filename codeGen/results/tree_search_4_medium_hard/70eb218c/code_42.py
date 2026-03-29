from functools import lru_cache

def min_operations(n, x):
    @lru_cache(None)
    def dp(x, n):
        if n == 1:
            return len(str(x))
        if len(str(x)) >= n:
            return -1
        res = float('inf')
        for y in range(10):
            res = min(res, dp(int(str(x) + str(y)), n-1) + 1)
        return res

    return dp(x, n)

if __name__ == "__main__":
    n, x = map(int, input().split())
    print(min_operations(n, x))
