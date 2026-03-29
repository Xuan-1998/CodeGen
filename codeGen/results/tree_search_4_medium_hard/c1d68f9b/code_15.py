import sys

n = int(sys.stdin.readline())
moods = list(map(int, sys.stdin.readline().split()))

dp = [float('inf')] * (n + 1)
dp[0] = 3  # minimum possible number of sides for an empty polygon

result = "NO"
for i in range(1, n + 1):
    if moods[i - 1]:
        dp[i] = min(dp[i], dp[i - 1] - 1)
    else:
        dp[i] = min(dp[i], dp[i - 1] + 1)
    if dp[i] > n:
        result = "NO"
        break
else:
    result = "YES"

print(result)
