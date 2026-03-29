def count_steady_tables(N, M):
    total_sum = N * (N + 1) // 2
    if total_sum > M:
        return 0

    result = 0
    for last_row_sum in range(M + 1):
        prev_row_sum = max(0, total_sum - last_row_sum)
        for row_sum in range(prev_row_sum, last_row_sum + 1):
            if row_sum * (N + 1) // 2 > M:
                break
            result += 1

    return result % (10**9 + 7)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(count_steady_tables(N, M))
