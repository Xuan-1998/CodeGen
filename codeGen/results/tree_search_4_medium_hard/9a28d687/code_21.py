import sys

n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[0][i] = costs[i]

for length in range(2, n + 1):
    for left in range(n - length + 1):
        right = left + length
        min_cost = sys.maxsize
        for k in range(left, right):
            # Option 1: Reverse s[k]
            cost = dp[0][k] if strings[left].startswith(strings[k][::-1]) else costs[k]
            # Option 2: Leave s[k] as it is
            if k > left:
                cost += dp[0][k - 1]
            min_cost = min(min_cost, cost)
        dp[0][right - 1] = min_cost

print(dp[0][-1])
