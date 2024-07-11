from sys import stdin, stdout

MOD = 998244353
N = int(stdin.readline())
d = list(map(int, stdin.readline().split()))

if d[0] != 1:
    stdout.write("0\n")
else:
    dp = [[0] * (N+1) for _ in range(N+1)]
    dp[0][0] = 1
    acc = [0] * (N+1)
    acc[0] = 1
    sz = [0] * (N+1)
    sz[0] = 1
    cnt = [0] * (N+1)
    cnt[1] = 1
    ans = 0
    for i in range(1, N):
        for j in range(i+1):
            dp[i][j] = acc[j] if j <= sz[i-1] else (acc[j] - dp[i-1][j-sz[i-1]]) % MOD
        sz[i] = sz[i-1] + d[i]
        acc = [0] * (N+1)
        for j in range(i+1):
            acc[j+1] = (acc[j] + dp[i][j]) % MOD
        cnt[i+1] = (cnt[i] * d[i]) % MOD
        ans = (ans + dp[i][i] * cnt[i+1]) % MOD
    stdout.write(str(ans) + "\n")

