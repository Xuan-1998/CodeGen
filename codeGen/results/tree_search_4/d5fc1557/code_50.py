def longestSubarray(nums):
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][i] = nums[i - 1]
        for j in range(i - 1, -1, -1):
            if nums[j] == 1:
                dp[j][i] = max(dp[j][i - 1], (dp[j + 1][i] if i > j + 1 else 0) + 1)
            else:
                dp[j][i] = dp[j][i - 1]
    return max(dp[0][-1])

def findLongestSubarray(nums):
    n = len(nums)
    max_length = 0
    for i in range(n):
        new_nums = nums[:i] + nums[i + 1:]
        max_length = max(max_length, longestSubarray(new_nums))
    return max_length

if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(findLongestSubarray(nums))
