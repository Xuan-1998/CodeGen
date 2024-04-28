import heapq
n, k = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(1, n):
    dp[i] = max(dp[i], dp[i - 1] + nums[i])
pq = [(nums[0], 0)]
for i in range(1, k + 1):
    for _ in range(i):
        v, j = heapq.heappop(pq)
        if j > 0:
            dp[j - 1] = max(dp[j - 1], dp[j] + v - nums[0])
    for j in range(k, i - 1, -1):
        if dp[j - 1] - (dp[j] - nums[i]) >= nums[i]:
            dp[j - 1] -= dp[j] - nums[i]
            heapq.heappush(pq, (-nums[i], j - 1))
    for _ in range(i):
        v, j = heapq.heappop(pq)
        if j > i:
            dp[j - 1] = max(dp[j - 1], dp[j] + v - nums[0])
print(max(0, *dp))
