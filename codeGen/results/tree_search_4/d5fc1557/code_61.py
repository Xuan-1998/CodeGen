===BEGIN CODE===
def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)  # Initialize the DP table with zeros

    for i in range(n - 1, -1, -1):  # Fill the DP table from end to start
        if i == n - 1:  # Base case when we're at the last element
            dp[i] = nums[i]
        elif nums[i] == nums[i + 1]:  # If consecutive elements are the same
            dp[i] = dp[i + 1] + 1  # Increase the length of the subarray
        else:  # Reset the subarray if we hit a different element
            dp[i] = 1

    return max(dp[0], dp[1:])  # Return the maximum subarray length

nums = [list(map(int, input().split())) for _ in range(int(input()))]
print(longest_subarray(nums))
===END CODE===
