n = int(input())
marks = list(map(int, input().split()))
dp = [0] * n

for i in range(1, n):
    dp[i] = min(dp[i-1] + (i - marks[i]), i)

print(dp[n-1])
