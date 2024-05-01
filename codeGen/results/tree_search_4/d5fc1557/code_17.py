from collections import defaultdict

def longestSubarray(nums):
    ones = sum(1 for num in nums if num == 1)
    max_length = 0
    prefix_sum = defaultdict(int)

    for i, num in enumerate(nums):
        if num == 1:
            ones -= 1
        prefix_sum[i] = ones
        max_length = max(max_length, max((prefix_sum[i-1] + 1) if i > 0 and ones > 0 else 0 for j in range(i)) if i > 0 else 0)

    return max_length

# Read input from standard input
nums = list(map(int, input().split()))

# Print the output to standard output
print(longestSubarray(nums))
