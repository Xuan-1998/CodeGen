def pivotIndex(nums):
    total_sum = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
        right_sum = total_sum - num - left_sum
        if left_sum == right_sum:
            return i
        left_sum += num

    return -1
