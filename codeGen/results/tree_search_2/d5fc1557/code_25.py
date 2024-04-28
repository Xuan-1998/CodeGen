def longest_subarray(nums):
    n = len(nums)
    memo = {0: 0}
    max_length = 0

    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            new_state = i if i not in memo else memo[i]
            memo[i] = max_length = max(max_length, new_state)
        else:
            max_length = 0

    return max_length - (n - max_length) if max_length != 0 else 0
