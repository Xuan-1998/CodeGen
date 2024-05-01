# Receive input from stdin
n = int(input())
nums = [int(x) for x in input().split()]

# Initialize dp and max_length
dp = [0] * (n + 1)
max_length = 0

for i in range(n):
    if nums[i] == 1:
        dp[i + 1] = max(dp[i], dp[i - 1] + 1) if i > 0 else 1
        max_length = max(max_length, dp[i + 1])
    else:
        dp[i + 1] = 0

# Return the length of the longest subarray containing only 1's after deleting one element
print(n - 1 - max_length)
