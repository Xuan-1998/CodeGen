from sys import stdin, stdout

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(min(i, n-i)+1):
        if j == 0:
            dp[i][j] = a[0]
        elif j == i//2 + 1:
            dp[i][j] = c[0]
        else:
            dp[i][j] = max(dp[i-1][k] + b[k+1] for k in range(j))

stdout.write(str(max(dp[n])))
