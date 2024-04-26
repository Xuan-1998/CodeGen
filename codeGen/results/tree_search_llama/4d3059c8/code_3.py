def pivotIndex(nums):
    total_sum = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        if left_sum == total_sum - num:
            return i
        left_sum += num
    return -1

# Read input from stdin
nums = [int(x) for x in input().split()]

# Print the pivot index to stdout
print(pivotIndex(nums))
