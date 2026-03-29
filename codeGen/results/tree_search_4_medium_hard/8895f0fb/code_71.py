import sys
from functools import lru_cache

@lru_cache(None)
def dp(i, k, l):
    if k > 0 and l > 0:
        return (1/(i+1)) * (dp(i-1, k-1, l) + dp(i-1, k, l-1) + dp(i-1, k-1, l-1))
    elif k > 0:
        return (1/(i+1)) * (2*dp(i-1, k-1, l))
    elif l > 0:
        return (1/(i+1)) * (2*dp(i-1, k, l-1))
    else:
        return 0

count = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(i):
        count[i] += j + i - j
expected_value = sum(count[i] * dp(i, 0, 0) for i in range(1, N + 1))
print(expected_value)
