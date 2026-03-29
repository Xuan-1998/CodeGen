from sys import stdin, stdout
MOD = 998244353
N = int(stdin.readline())
d = list(map(int, stdin.readline().split()))
d = [0] + d
if d[1] != 1 or d[0] != 0:
    stdout.write("0\n")
    exit(0)
c = [[0]*(N+1) for _ in range(N+1)]
c[0][0] = 1
for i in range(1, N+1):
    c[i][0] = 1
    for j in range(1, i+1):
        c[i][j] = (c[i-1][j-1] + c[i-1][j]) % MOD
dp = [0]*(N+1)
dp[0] = 1
s = [0]*(N+2)
for i in range(1, N+1):
    for j in range(i, -1, -1):
        dp[j] = dp[j]*c[s[i]-s[i-1]][d[i]] % MOD
        if j:
            dp[j] = (dp[j] + dp[j-1]*c[s[i]-s[i-1]+d[i]-1][d[i]-1]) % MOD
    s[i+1] = s[i] + d[i]
stdout.write(str(dp[d[N]])+"\n")

