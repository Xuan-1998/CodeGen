n = int(input())
marks = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(2, n + 1):
    above_water = max(0, marks[i - 1] - marks[i - 2])
    dp[i] = min(dp[i - 1], above_water)

print(sum(marks[:i]) - dp[i] for i in range(1, n + 1))[n - 1]
