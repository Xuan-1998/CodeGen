from collections import deque

n = int(input())
dp = [float('inf')] * n
dp[0] = 0  # capital city is always reachable with 0 reversed edges

for _ in range(n - 1):
    u, v = map(int, input().split())
    dp[v - 1] = min(dp[v - 1], dp[u - 1] + 1)

max_depth = max(dp)  # find the maximum depth from the capital
print(max_depth)

# print all possible ways to choose the capital (not required for this problem)
