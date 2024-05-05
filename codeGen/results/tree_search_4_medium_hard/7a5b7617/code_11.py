def dp(n_rows, prev_row_sum):
    if n_rows > N or prev_row_sum >= M:
        return 1

    total_ways = 0
    for row_sum in range(prev_row_sum + 1, M + 1):
        if n_rows - 1 == N:  # base case: all rows are filled
            total_ways += (M - prev_row_sum) % 1000000000  # calculate the number of ways to fill the remaining table
        else:
            total_ways += dp(n_rows - 1, row_sum)
    return total_ways

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    result = dp(N, 0) % 1000000000
    print(result)
