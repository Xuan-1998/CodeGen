def longest_subarray(nums):
    n = len(nums)
    dp = [[0] * 2 for _ in range(n)]

    max_length = 0

    for i in range(n):
        if nums[i] == 1:
            dp[i][1] = dp[i-1][1] + 1 if i > 0 else 1
        else:
            dp[i][0] = 0

        max_length = max(max_length, dp[i][1])

    return max_length - 1 if max_length > 0 else 0

# Read input from stdin and print the result to stdout
n = int(input())
nums = list(map(int, input().split()))
print(longest_subarray(nums))
