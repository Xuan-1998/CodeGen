def longest_subarray(nums):
    n = len(nums)
    ans = 0
    i, j = 0, 0
    while j < n:
        if nums[j] == 1:
            j += 1
        else:
            if i <= j:
                ans = max(ans, j - i + 1)
            i = j + 1
    return ans
