import itertools

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(min(i // K, M + 1) + 1):
        if all(abs(A[x] - A[y]) <= M for x in range(j * K - 1, i) for y in range(x + j * K, i)):
            dp[i][j] = True

print(any(dp[N]))
