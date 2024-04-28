import sys

def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [0] * (k + 1)
    curr_max = nums[0]

    for i in range(1, n):
        for j in range(min(i, k), -1, -1):
            if i - j >= 0:
                curr_max = max(curr_max, nums[i] + dp[j])
            dp[j] = max(dp[j], curr_max - nums[i])
    return curr_max

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(max_sum_subsequence(nums, k))
