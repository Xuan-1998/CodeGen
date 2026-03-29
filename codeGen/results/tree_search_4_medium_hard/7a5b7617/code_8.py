from functools import lru_cache

@lru_cache(None)
def dp(n_rows, prev_row_sum):
    if n_rows == 0:
        return 1
    if prev_row_sum > M:
        return 1
    res = 0
    for row_sum in range(prev_row_sum + 1, M + 1):
        res += (M - row_sum + 1)
    return res % 1000000000

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(dp(N-1, 0))
