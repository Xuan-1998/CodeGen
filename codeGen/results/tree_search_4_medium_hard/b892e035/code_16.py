import sys
from functools import lru_cache

@lru_cache(None)
def dp(n, a, b):
    if n == 0:
        return 1.0  # base case: all tickets numbered correctly
    p1, num1, num2 = float(next(sys.stdin).split()[1]), int(next(sys.stdin).split()[1]), int(next(sys.stdin).split()[2])
    p2 = 1 - p1  # probability of the other number

    if a == b:  # same number for both options
        prob = dp(n-1, a+1, a+1) * (p1 if a > 0 else 0.5)
    else:
        prob = dp(n-1, a+1, a+1) * p1 + dp(n-1, b+1, b+1) * p2

    return prob

T = int(next(sys.stdin).split()[0])
for _ in range(T):
    n = int(next(sys.stdin))
    result = 0.0
    for i in range(n):
        a, _, _ = map(int, next(sys.stdin).split())
        result += dp(n-i-1, 1, 1) * (a/100)
    print(round(result, 6))  # ignore rounding errors < 10^-6
