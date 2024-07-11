from sys import stdin, stdout

MOD = 998244353
N = int(stdin.readline())
D = list(map(int, stdin.readline().split()))

if D[0] != 1 or D[1] < 1:
    stdout.write("0\n")
    exit(0)

cnt = [0]*(N+1)
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    cnt[i] = cnt[i-1] + D[i-1]

for i in range(1, N):
    if D[i] > cnt[i] or D[i] > N-cnt[i-1]:
        stdout.write("0\n")
        exit(0)
    for j in range(cnt[i]):
        for k in range(min(j, D[i])+1):
            dp[i][j] = (dp[i][j] + dp[i-1][j-k]*dp[i-1][D[i]-1-k]) % MOD

ans = 0
for i in range(N):
    ans = (ans + dp[N-1][i]) % MOD

stdout.write(f"{ans}\n")

