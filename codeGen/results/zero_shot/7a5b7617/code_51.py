T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    max_row_sum = min(M, N * (N + 1) // 2)
    max_element_value = min(max_row_sum, M)
    from math import comb
    result = 1
    for i in range(N):
        result = (result * (M - i)) // (i + 1)
    print((comb(M, N - 1) * result) % 1000000000)
