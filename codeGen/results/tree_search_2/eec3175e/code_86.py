from functools import lru_cache

def is_divisible_by_m(n, m):
    @lru_cache(None)
    def dp(i, total):
        if i == 0:
            return total % m == 0
        return (dp(i - 1, total) or 
                dp(i - 1, total + arr[i - 1]))

    arr = [int(x) for x in input().split()]
    n = len(arr)
    return "1" if dp(n, 0) else "0"

n, m = map(int, input().split())
print(is_divisible_by_m(n, m))
