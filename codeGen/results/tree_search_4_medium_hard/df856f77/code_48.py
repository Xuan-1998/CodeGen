===BEGIN CODE===
from sys import stdin, stdout

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

dp = [0] * (n + 1)

for i in range(1, n):
    dp[i] = float('inf')
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = min(dp[i], dp[j] + abs(arr[i] - arr[j]))
        elif arr[j] == arr[i]:
            dp[i] = 0

stdout.write(str(dp[-1]) + '\n')
===END CODE===
