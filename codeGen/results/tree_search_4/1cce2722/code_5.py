from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)
memo = defaultdict(int)

for i in range(n):
    max_points = 0
    for j in range(i, -1, -1):
        if a[j] not in a[:j]:
            max_points = max(max_points, memo.get(dp[j-1], 0) + (i-j+2))
    dp[i+1] = max_points

print(dp[-1])
