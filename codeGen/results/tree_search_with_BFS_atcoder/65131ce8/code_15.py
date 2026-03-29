import sys
MOD = 998244353
N = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split()))
comb = [[0 for _ in range(N+1)] for _ in range(N+1)]
comb[0][0] = 1
for i in range(1, N+1):
    comb[i][0] = 1
    for j in range(1, N+1):
        comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
dp[1][1] = 1
for i in range(2, N+1):
    for j in range(1, i+1):
        for k in range(1, i):
            if d[i-1] != k-1:
                continue
            for l in range(1, j+1):
                dp[i][j] = (dp[i][j] + dp[k][l] * comb[i-1][k-1] * dp[i-k][j-l]) % MOD
answer = sum(dp[N][j] for j in range(1, N+1)) % MOD
sys.stdout.write(str(answer) + '\n')

