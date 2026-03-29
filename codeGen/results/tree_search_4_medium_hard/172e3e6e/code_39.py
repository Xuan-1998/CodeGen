from functools import lru_cache

@lru_cache(None)
def good_subsequences(n, last_divisor):
    if n == 0:
        return 1
    result = 0
    for i in range(last_divisor + 1, n + 1):
        if n % i == 0:  # i is a divisor of n
            result += good_subsequences(n - i, i)
    return result

n = int(input())
a = list(map(int, input().split()))

print(good_subsequences(n, 0) % (10**9 + 7))
