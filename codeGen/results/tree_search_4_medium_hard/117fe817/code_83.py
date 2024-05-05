n = int(input())  # receive input from stdin

dp = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(i - 1, 0, -1):
        if (i - 1) // 10 == j:
            dp[i] += 1
        dp[i] += dp[j]

print(dp[n])  # print the result to stdout
