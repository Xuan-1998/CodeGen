import sys

n, q = map(int, input().split())
signs = list(input())

dp = [[0] * (q + 1) for _ in range(n)]

for i in range(1, n):
    dp[i][0] = signs[i-1]

for j in range(1, q+1):
    l, r = map(int, input().split())
    for i in range(l-1, r):
        if signs[i] == "+":
            dp[i][j] += 1
        else:
            dp[i][j] -= 1

for j in range(1, q+1):
    l, r = map(int, input().split())
    print(min(dp[min(l-1, r)][max(0, min(l-1, r)-j)] for j in range(max(0, min(l-1, r)-l+1), r)))
