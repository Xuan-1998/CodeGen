n = int(input())
marks = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = float('inf')
    for j in range(i):
        if marks[j] < i:
            dp[i] = min(dp[i], dp[j] + (i - j) * marks[i - 1])

print(dp[n])
