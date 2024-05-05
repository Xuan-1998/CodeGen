import sys

def longest_increasing_subsequences(nums):
    n = len(nums)
    dp = [1] * n  # Initialize DP table with all ones (single-element subsequences)

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)  # Update DP[i] as needed

    max_length = max(dp)
    count = sum(1 for x in dp if x == max_length)

    return count

# Read input from stdin
input_line = sys.stdin.readline().strip()
nums = list(map(int, input_line.split()))

print(longest_increasing_subsequences(nums))
