def num_steady_tables(N, M):
    memo = {(i, j): 0 for i in range(2) for j in range(M+1)}
    memo[(0, 0)] = 1

    for i in range(1, N):
        for j in range(1, M+1):
            if j < i:
                continue
            if j > i:
                memo[(i, j)] = 0
                continue
            for k in range(i):
                memo[(i, j)] += memo.get((k, j-k), 0)
            memo[(i, j)] %= 1_000_000_000

    return memo[(N-1, M)]

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(num_steady_tables(N, M))
