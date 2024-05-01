def longest_ones(nums):
    memo = {0: 0}
    max_length = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            if i > 0 and nums[i-1] == 0:
                max_length = 1
            else:
                for j in range(i):
                    if memo.get(j, 0) == 1:
                        max_length = max(max_length, memo[j] + 1)
        elif nums[i] == 0:
            max_length = 0
        memo[i] = max_length

    return max_length
