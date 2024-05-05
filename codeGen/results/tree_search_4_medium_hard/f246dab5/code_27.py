import sys

n = int(sys.stdin.readline())
dp = [0]

for i in range(1, n+1):
    t_i = int(sys.stdin.readline())

    if t_i >= 90:
        dp.append(min(dp[-1], min(dp[j-1] for j in range(i) if t_j <= t_i)) + (t_i - 60)*50)
    else:
        dp.append(min(dp[-1], min(dp[j-1] for j in range(i) if t_j <= t_i)) + 20)

print(dp[-1])
