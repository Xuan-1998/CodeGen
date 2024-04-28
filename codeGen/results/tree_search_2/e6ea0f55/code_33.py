import sys

def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [[-sys.maxsize for _ in range(k+1)] for _ in range(n)]

    dp[0][0] = nums[0]
    for i in range(1, n):
        for j in range(min(i, k)+1):
            dp[i][j] = max(dp[i-1][k-j] + nums[i], dp[i-1][j])

    return max(max(row) for row in dp)

# Test the function
nums = list(map(int, input().split()))
k = int(input())
print(max_sum_subsequence(nums, k))
