from sys import stdin, maxint
N, K, M = map(int, stdin.readline().split())
A = list(map(int, stdin.readlines()))
dp = [[False for _ in range(K+1)] for _ in range(N)]

dp[0][K] = True

for i in range(1, N):
    for k in range(min(i+1, K), 0, -1):
        if dp[i-1][k-1]:
            if maxint == M:
                dp[i][k] = (A[i-1] - A[0] <= M)
            else:
                dp[i][k] = (A[i-1] - A[0] <= M) and (dp[i-1][k-1])
        else:
            break
print(dp[N-1][K])
