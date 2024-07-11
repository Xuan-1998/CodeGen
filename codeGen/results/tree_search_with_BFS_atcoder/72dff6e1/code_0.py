MOD = 998244353
N = int(input())
A = list(map(int, input().split()))
A = [0] + A
dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1

for i in range(N):
    for j in range(i+1):
        for k in range(j+1):
            if dp[i][j][k] == 0:
                continue
            # Use a new number
            dp[i+1][j+1][k] = (dp[i+1][j+1][k] + dp[i][j][k]) % MOD
            if k+1 <= A[i+1]:
                dp[i+1][j+1][k+1] = (dp[i+1][j+1][k+1] + dp[i][j][k]) % MOD
            # Use the same number again
            if j+1 <= A[i+1]:
                dp[i+1][j][k] = (dp[i+1][j][k] + dp[i][j][k]) % MOD
                if k+1 <= A[i+1]:
                    dp[i+1][j][k+1] = (dp[i+1][j][k+1] + dp[i][j][k]) % MOD

answer = 0
for j in range(N+1):
    for k in range(j+1):
        answer = (answer + dp[N][j][k]) % MOD

print(answer)

