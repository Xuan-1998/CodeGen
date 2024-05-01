import sys

def subset_sum(n, nums):
    seen = set()
    dp = [[False] * (sum(nums) + 1) for _ in range(n + 1)]
    
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(sum(nums) + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    
    sums = set()
    for i in range(n + 1):
        for j in range(sum(nums) + 1):
            if dp[i][j]:
                seen.add(j)
    
    return ' '.join(map(str, sorted(seen)))

n = int(input())
nums = list(map(int, input().split()))
print(subset_sum(n, nums))
