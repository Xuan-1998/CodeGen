N = int(input())
D = list(map(int, input().split()))
MOD = 998244353

prefix = [0]*(N+1)
for i in range(N-1, -1, -1):
    prefix[i] = prefix[i+1] + D[i]

dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(prefix[i+1]+1):
        for k in range(min(j, D[i])+1):
            dp[i+1][j-k+D[i+1]] += dp[i][j] * comb(j, k) * comb(prefix[i+1]-j+1, D[i+1])
            dp[i+1][j-k+D[i+1]] %= MOD

good = [0]*N
for i in range(N):
    for j in range(prefix[i+1]+1):
        good[i] += dp[i][j] * comb(prefix[i+1], j)
        good[i] %= MOD

answer = 0
for i in range(N):
    answer += good[i] * D[i]
    answer %= MOD

print(answer)

