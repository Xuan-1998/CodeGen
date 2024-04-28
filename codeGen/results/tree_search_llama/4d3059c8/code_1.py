def pivotIndex(nums):
    n = len(nums)
    total_sum = sum(nums)
    prefix_sum = 0

    # Calculate the prefix sum array
    for i in range(n):
        if prefix_sum == total_sum - prefix_sum:
            return i
        prefix_sum += nums[i]

    return -1

