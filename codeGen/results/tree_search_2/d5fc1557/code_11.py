def maximum_ones(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    max_length = 0
    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 0
        max_length = max(max_length, dp[i])
    return max_length

def find_max_ones(nums):
    n = len(nums)
    left, right = 0, n - 1
    max_length = 0
    while left <= right:
        if nums[left] == 1 and nums[right] == 1:
            max_length = max(max_length, right - left + 1)
            left += 1
            right -= 1
        elif nums[left] == 1:
            left += 1
        else:
            right -= 1
    return max_length

def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 0
    return max(dp)

def remove_element(nums):
    n = len(nums)
    for i in range(n-1, -1, -1):
        if nums[i] == 0:
            del nums[i]
            break
    return len(nums)

def longest_subarray_after_deletion(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 0
    max_length = 0
    for i in range(n, -1, -1):
        if nums[i] == 1 and dp[n-1] > max_length:
            max_length = dp[n-1]
            break
    return max_length

def solve(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] == 0:
            nums.pop(i)
            i -= 1
            break
    return longest_subarray(nums)

# Read input from standard input.
nums = list(map(int, input().split()))
print(solve(nums))
