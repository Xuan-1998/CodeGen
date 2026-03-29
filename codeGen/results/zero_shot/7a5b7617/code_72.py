import sys

def count_steady_tables(N, M):
    count = 1
    for i in range(1, N):
        # the ith row sum must be at least as large as the (i-1)th row sum
        min_row_sum = max(0, (i-1)*M + i)
        count *= (M - (i-1)*M // i + 1)
    return count % 1000000000

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(count_steady_tables(N, M))
