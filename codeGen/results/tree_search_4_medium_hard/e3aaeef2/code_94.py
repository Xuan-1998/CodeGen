import sys

dp = [[0 for _ in range(int(2e5)+1)] for _ in range(int(1e9+7))]

dp[0][0] = 1

for i in range(1, int(1e9+7)):
    for k in range(1, int(2e5)+1):
        if i < 10:
            dp[i][k] = min(dp[i][k-1], dp[i*10 + (i+1)%10][k-1]) + 1
        else:
            last_digit = int(str(i)[-1])
            dp[i][k] = min(dp[last_digit*10+(last_digit+1)%10][k-1], dp[i//10][k-1]) + 1

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print((dp[n][m]) % (int(1e9+7)))
