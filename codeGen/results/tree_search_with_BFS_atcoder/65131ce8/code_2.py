N = int(input())
d = list(map(int, input().split()))
d = [0] + d

MOD = 998244353
dp = [[0]*(N+1) for _ in range(N+1)]
good = [[0]*(N+1) for _ in range(N+1)]
prefix = [0]*(N+1)

dp[1][1] = 1
good[1][1] = 1
for i in range(2, N+1):
    prefix[0] = dp[i-1][0]
    for j in range(1, i):
        prefix[j] = (prefix[j-1] + dp[i-1][j]) % MOD
    for j in range(1, i+1):
        dp[i][j] = dp[j-1][j-1] * (prefix[i-1] - prefix[j-1]) % MOD
        good[i][j] = (good[j-1][j-1] * (prefix[i-1] - prefix[j-1]) + dp[j-1][j-1] * (prefix[i-1] - prefix[j-1])) % MOD

answer = sum(good[N]) % MOD
print(answer)

