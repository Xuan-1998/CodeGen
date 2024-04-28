def longest_subarray(nums):
    n = len(nums)
    if not nums:  # Edge case for an empty array
        return 0

    max_length = 0
    current_length = 0

    for num in nums:
        if num == 1:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 0

    # Handle the case where the array ends with a sequence of ones
    max_length = max(max_length, current_length)

    return n - 2 if max_length == 0 else max_length

