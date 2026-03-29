N = int(input())
A = list(map(int, input().split()))
mod = 998244353

dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1

for i in range(N):
    new_dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
    for j in range(i+1):
        for k in range(j+1):
            # if the last number is used again
            if k <= A[i]:
                new_dp[i+1][j][k] = (new_dp[i+1][j][k] + dp[i][j][k]*(j-k+1)) % mod
            # if a new number is used
            if j < A[i]:
                new_dp[i+1][j+1][k] = (new_dp[i+1][j+1][k] + dp[i][j][k]*(j+1)) % mod
    dp = new_dp

answer = sum(sum(dp[N][j][k] for k in range(j+1)) for j in range(N+1)) % mod
print(answer)

