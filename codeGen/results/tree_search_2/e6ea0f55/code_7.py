import sys

# Read input
nums = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

# Calculate the result
result = maxSumSubsequence(nums, k)

# Print the result
print(result)
