import sys

n, t = map(int, input().split())
fractional_part = [int(x) for x in str(input()).split('.')[1]]

dp = [[0] * (t + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(t + 1):
        if i == 1:
            dp[i][j] = min(fractional_part[0], 9)
        else:
            prev_grade = dp[i - 1][min(j, t)]
            rounded_grade = max(prev_grade, fractional_part[i - 1])
            dp[i][j] = max(dp[i - 1][k] + rounded_grade for k in range(min(j, t), j + 1))
print(max(dp[n]))
