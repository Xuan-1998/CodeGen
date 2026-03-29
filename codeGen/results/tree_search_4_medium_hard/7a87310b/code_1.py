from functools import lru_cache

def pos_det_count(n):
    @lru_cache(None)
    def dp(i, j, trace_value):
        if i + j == 2:
            return 1 if i > 0 and (i == j or j > 2) else 0
        total = 0
        for k in range(3):
            if k != i and k != j:
                total += dp(i, k, trace_value - 1)
        return total

    result = 0
    for i in range(1, n + 1):
        if i % 2 == 0:  # positive determinant
            result += dp(0, 2, i)
        else:
            result += dp(1, 1, i)

    return result

T = int(input())
for _ in range(T):
    N = int(input())
    print(pos_det_count(N))
