def can_sum_divisible(n, m):
    # Initialize a boolean array dp of size m+1 with all False values.
    # dp[i] will be True if there exists a subset sum i modulo m.
    dp = [False] * (m + 1)
    dp[0] = True  # Base case: The sum 0 is divisible by m.

    for num in range(n):
        for i in range(m, -1, -1):  # Start from the right
            if i >= nums[num]:  # If the current number fits within the remaining sum
                dp[i] = dp[i] or dp[i - nums[num]]  # Update the boolean value

    return dp[m]

# Read input
n, m = map(int, input().split())
nums = list(map(int, input().split()))

print(can_sum_divisible(n, m))
