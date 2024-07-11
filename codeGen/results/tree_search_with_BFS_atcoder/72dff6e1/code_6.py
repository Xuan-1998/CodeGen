MOD = 998244353
N = int(input())
A = list(map(int, input().split()))

dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1

for i in range(N):
    dp_new = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
    for j in range(i+1):
        for k in range(i+1):
            if dp[i][j][k] == 0:
                continue
            
            # The current element is new and appears more than once
            dp_new[i+1][j+1][k] += dp[i][j][k] * max(A[i] - 1 - k, 0)
            dp_new[i+1][j+1][k] %= MOD
            
            # The current element is new and appears exactly once
            dp_new[i+1][j+1][k+1] += dp[i][j][k] * (N - j)
            dp_new[i+1][j+1][k+1] %= MOD
            
            # The current element has appeared before
            dp_new[i+1][j][k] += dp[i][j][k] * max(j - k, 0)
            dp_new[i+1][j][k] %= MOD
            
            # The current element has appeared exactly once before
            if k > 0:
                dp_new[i+1][j][k-1] += dp[i][j][k] * k
                dp_new[i+1][j][k-1] %= MOD
    dp = dp_new

answer = 0
for j in range(N+1):
    for k in range(N+1):
        answer += dp[N][j][k]
        answer %= MOD

print(answer)

