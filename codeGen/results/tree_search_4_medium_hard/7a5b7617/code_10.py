def dp(n_rows, prev_row_sum):
    if (n_rows, prev_row_sum) in memo:
        return memo[(n_rows, prev_row_sum)]

    if n_rows == 0 or prev_row_sum >= M:
        return 1

    result = 0
    for s in range(M + 1):
        if s <= M and prev_row_sum + s <= M:
            result += dp(n_rows - 1, prev_row_sum + s)
    memo[(n_rows, prev_row_sum)] = result % 1000000000

    return memo[(n_rows, prev_row_sum)]

T = int(input())
memo = {}
for _ in range(T):
    N, M = map(int, input().split())
    print(dp(N, 0) % 1000000000)
