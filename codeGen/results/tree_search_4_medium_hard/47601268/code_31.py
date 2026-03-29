from functools import lru_cache

def count_binary_numbers(n):
    @lru_cache(None)
    def helper(i):
        if i < 0:
            return 0
        if i == 0:
            return 1
        if (i & (i << 1)) and not (i & (i >> 1)):
            return helper(i-1) + 1
        else:
            return helper(i-1)

    return helper(n)
