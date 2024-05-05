from sys import stdin, stdout
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp = [0] * (n+1)
dp[0] = 0
for i in range(n):
    if dp[i] > -arr[i]:
        dp[i + 1] = min(dp[i], dp[i] - arr[i])
    else:
        dp[i + 1] = 0
if dp[n-1] >= 0:
    stdout.write('Yes\n')
else:
    stdout.write('No\n')
