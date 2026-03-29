from functools import lru_cache

def min_operations(n, x):
    @lru_cache(None)
    def dp(s):
        if len(s) == n:
            return 0
        res = float('inf')
        for i in range(1, 10):
            new_s = str(int(s) * i)
            res = min(res, 1 + dp(new_s))
        return -1 if res == float('inf') else res

    return dp(str(x))

if __name__ == "__main__":
    n, x = map(int, input().split())
    print(min_operations(n, x))
