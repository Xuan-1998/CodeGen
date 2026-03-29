code = '''
import sys
from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 2:
        return 1
    return 1 + f(n // 2)

t, l, r = map(int, input().split())
print((f(t) - f(l)) % (10**9 + 7))
'''
