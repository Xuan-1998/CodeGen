from collections import defaultdict
from functools import lru_cache

@lru_cache(maxsize=None)
def dp(n, carry):
    if n == 0:
        return 1 if carry else 0
    res = 0
    for d in range(10):
        if d + carry >= 10:
            res += 1
        carry = (d + carry) // 10
    return res

def expected_carries(N):
    total_pairs = 10 ** N * 10 ** N
    total_carry = sum(dp(n, 0) for n in range(N+1))
    return total_carry / total_pairs


T = int(input())
for _ in range(T):
    N = int(input())
    print(expected_carries(N))
