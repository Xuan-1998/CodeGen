from collections import defaultdict

def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    dp = defaultdict(int)
    for num in nums:
        dp[num] = 1
        for prev_num in sorted(dp.keys()):
            if num > prev_num:
                dp[num] = max(dp.get(num, 0), dp[prev_num] + 1)

    return max(dp.values())

# Read input from stdin
nums = [int(x) for x in input().split()]

# Print the answer to stdout
print(longest_increasing_subsequence(nums))
