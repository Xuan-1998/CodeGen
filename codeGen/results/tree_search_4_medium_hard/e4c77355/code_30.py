import sys

def lis(nums):
    n = len(nums)
    dp = [1] * n
    memo = {}

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        memo[i] = dp[i]

    return max(memo.values())

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    print(lis(nums))
