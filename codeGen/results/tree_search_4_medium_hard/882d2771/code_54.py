code = '''
import math

t, l, r = map(int, input().split())

def f(n):
    if n <= 1:
        return 0
    if n % 3 == 1:
        return 1 + f(math.floor((n - 1) / 3))
    elif n % 3 == 2:
        return 1 + f(math.floor((n - 2) / 3))
    else:
        return 1 + f(math.floor(n / 3))

print((t * (f(r) - l)) % (10**9 + 7))
'''

