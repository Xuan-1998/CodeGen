from functools import lru_cache

@lru_cache(None)
def count_ones(n):
    if n < 10:
        return int(str(n).count('1'))
    return count_ones(n // 10) + (n % 10 == 1)

n = int(input())
print(count_ones(n))
