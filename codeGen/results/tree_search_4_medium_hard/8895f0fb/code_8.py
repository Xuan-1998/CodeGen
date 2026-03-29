import sys
from functools import lru_cache

def expected_carries(N):
    @lru_cache(None)
    def dp(i, j):
        if i == 0 or j == 0:
            return 0
        a = int(str(A)[i-1])
        b = int(str(B)[j-1])
        carry = max(a, b) - min(a, b)
        return (carry > 0) + dp(i-1, j-1)

    A = int(input())
    B = int(input())
    total_carries = sum((dp(N, i) for i in range(1, N+1)))
    expected_value = total_carries / (N * (N+1) // 2)
    print(f"{expected_value:.6f}")
