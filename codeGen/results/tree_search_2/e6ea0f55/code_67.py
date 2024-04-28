from collections import deque

def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]
    queue = deque([(0, 0)])

    while queue:
        i, j = queue.popleft()
        dp[i][j] = nums[i]
        
        if i > 0 and j > 0:
            for prev_i in range(i):
                if abs(nums[prev_i] - nums[i]) <= k * j:
                    dp[i][j] = max(dp[i][j], dp[prev_i][j-1] + nums[i])
                    
        if i < n-1 and j > 0:
            for next_i in range(i+1, n):
                if abs(nums[next_i] - nums[i]) <= k * j:
                    queue.append((next_i, j-1))
                    
    return max(max(row) for row in dp)
