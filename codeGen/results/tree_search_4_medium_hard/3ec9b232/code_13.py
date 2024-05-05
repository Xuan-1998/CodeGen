import math

n = int(input())
M = list(map(int, input().split()))
count_m = sum(1 for x in M if x == 1) # count the number of elements equal to 1
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    dp[i] = 0
    for j in range(i):
        if M[j] == 1:
            dp[i] += dp[j]
        else:
            dp[i] += dp[j - 1]

print(dp[n])
