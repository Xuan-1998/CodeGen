import sys

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[[False] * (M + 1) for _ in range(N + 1)] for _ in range(K + 1)]

for i in range(1, N + 1):
    for j in range(min(i, K), 0, -1):
        if A[i - 1] - M <= A[0] <= A[i - 1] + M:
            for k in range(j - 1, i):
                if dp[k][j - 1]:
                    dp[i][j] = True
                    break

print("Yes" if any(dp[N][i] for i in range(1, K + 1)) else "No")
