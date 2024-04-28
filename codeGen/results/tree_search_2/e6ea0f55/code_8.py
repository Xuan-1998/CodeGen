import sys

def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        for j in range(min(i+1, k)+1):
            if i == 0:
                dp[i][j] = nums[0]
            else:
                dp[i][j] = max(dp[i-1][j-1] + nums[i] if j > 0 else 0,
                               dp[i-1][j] + nums[i])
    return max(max(row) for row in dp)

if __name__ == "__main__":
    k, *nums = map(int, input().split())
    print(max_sum_subsequence(nums, k))
