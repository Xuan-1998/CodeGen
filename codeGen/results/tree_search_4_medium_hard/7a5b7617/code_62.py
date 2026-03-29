from math import comb

def solve(N, M):
    total_sum = N * M
    count = 0
    for row_sum in range(M, total_sum + 1):
        if all(row_sum <= sum(row) for row in [[i] * (M // N) + [i + 1] * (N - i) for i in range(N)]):
            count += comb(total_sum, row_sum)
    return count % 10**9 + 7

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(solve(N, M))
