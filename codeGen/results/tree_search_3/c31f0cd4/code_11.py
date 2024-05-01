def subsetSums(nums):
    n = len(nums)
    dp = [[False] * (sum(nums) + 1) for _ in range(n + 1)]
    
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(sum(nums) + 1):
            if j == 0:
                dp[i][j] = True
            elif nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
    
    return [j for i in range(n + 1) for j in range(sum(nums) + 1) if dp[i][j]]

# Read input and print output
N = int(input())
nums = list(map(int, input().split()))
print(' '.join(map(str, subsetSums(nums))))
