def longest_subarray(nums):
    max_len = 0
    current_streak = 0

    for num in nums:
        if num == 1:
            current_streak += 1
            max_len = max(max_len, current_streak)
        else:
            if current_streak > 0:
                max_len = max(max_len, current_streak)
            current_streak = 0

    return max_len

def longest_subarray_after_deletion(nums):
    n = len(nums)

    # Find the longest subarray containing only 1's
    max_len = 0
    for i in range(n):
        if nums[i] == 0:
            continue
        current_streak = 1
        for j in range(i+1, n):
            if nums[j] == 0:
                break
            current_streak += 1
        max_len = max(max_len, current_streak)

    # If no subarray containing only 1's is found, return 0
    if max_len == 0:
        return 0

    # Find the longest subarray containing only 1's after deleting one element
    for i in range(n):
        if nums[i] == 0:
            continue
        current_streak = 1
        for j in range(i+1, n):
            if nums[j] == 0:
                break
            current_streak += 1
        max_len_after_deletion = max(max_len_after_deletion, current_streak)

    return max_len_after_deletion

n = int(input())
nums = [int(x) for x in input().split()]

print(longest_subarray_after_deletion(nums))
