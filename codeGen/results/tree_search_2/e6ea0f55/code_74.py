import sys

def maxSubsequenceSum(nums, k):
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][i] = nums[i - 1] if i > 0 else 0

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length
            max_sum = nums[j - 1]
            for ii in range(i, j):
                if (j - ii) <= k:
                    max_sum = max(max_sum, dp[i][ii] + nums[ii])
            dp[i][j] = max_sum

    return max_sum

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    print(maxSubsequenceSum(nums, k))
