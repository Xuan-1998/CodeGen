import sys
from collections import defaultdict

def solve(n, k, m, p):
    dp = [[[0 for _ in range(m+1)] for _ in range(k+1)] for _ in range(n+1)]
    c = [0] + list(map(int, input().split()))
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j][m] = max(dp[i-1][j-1][m] + p[i]*c[j], dp[i-1][j][m])
    total_money = 0
    accepted_requests = 0
    tables_used = [False]*(k+1)
    for i in range(n, -1, -1):
        for j in range(k, -1, -1):
            if dp[i][j][m] > dp[i-1][j][m]:
                total_money += p[i]*c[j]
                accepted_requests += 1
                tables_used[j] = True
                break
    print(accepted_requests, total_money)
    for i in range(n, -1, -1):
        for j in range(k, -1, -1):
            if dp[i][j][m] > dp[i-1][j][m]:
                print(i, j)
                break

n = int(input())
p = [0] + list(map(int, input().split()))
k = int(input())
m = int(input())

solve(n, k, m, p)
