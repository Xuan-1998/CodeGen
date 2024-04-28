def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        for j in range(min(i + 1, k + 1)):
            if i < j:
                dp[i][j] = dp[i - 1][min(j - 1, k)] + nums[i]
            else:
                dp[i][j] = nums[i]

    return max(max(row) for row in dp)

if __name__ == "__main__":
    k = int(input())
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(maxSumSubsequence(nums, k))
