n = int(input())
marks = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = min(dp[i-1], marks[i-1] - i)
print(sum([i for i in dp[1:] if i]))
