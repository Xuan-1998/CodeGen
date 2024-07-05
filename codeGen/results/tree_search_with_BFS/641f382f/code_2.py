from math import gcd
from sys import stdin, stdout

def solve():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    dp = [[0]*n for _ in range(n)]
    g = [[0]*n for _ in range(n)]
    for i in range(n):
        g[i][i] = a[i]
        if a[i] == 1:
            stdout.write('1\n')
            return
    for length in range(1, n):
        for i in range(n-length):
            j = i + length
            g[i][j] = gcd(g[i][j-1], a[j])
            if g[i][j] == 1:
                dp[i][j] = length
                continue
            dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
    if dp[0][n-1] >= n:
        stdout.write('-1\n')
    else:
        stdout.write(str(dp[0][n-1]+n)+'\n')

solve()

