n = int(input())
marks_above_water = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = min(dp[j] + (i - j - 1) * j for j in range(i))

print(min(marks_above_water[i] - i for i in range(n)))
