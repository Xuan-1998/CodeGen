dp = [-1] * (A + 1)
dp[0] = 0

for i in range(1, A // 2 + 1):
    for j in range(A - i + 1):
        if ((j ^ i) == B):
            dp[i] = min(dp.get(i, float('inf')), j)

x = dp[A]
if (x < 0):
    print(-1)
else:
    y = A - x
    print(f"{x} {y}")
