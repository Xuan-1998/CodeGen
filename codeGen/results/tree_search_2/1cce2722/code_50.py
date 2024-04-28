n = int(input())
sequence = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    if i > 0:
        dp[i] = max(dp[i-1], sequence[i])
    else:
        dp[i] = sequence[i]

max_points = 0
current_points = sequence[0]
for i in range(1, n):
    if current_points == sequence[i]:
        current_points += 1
    else:
        max_points = max(max_points, current_points)
        current_points = sequence[i]

print(max(max_points, dp[-1]))
