code
n = int(input())
marks = list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(i):
        if marks[j] < j:
            dp[i] = min(dp[i], dp[j - 1] + (i - j) * marks[i - 1] - dp[j - 1])
print(min(dp))
