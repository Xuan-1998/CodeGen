def longest_subarray(nums):
    memo = {}

    def helper(i):
        n = len(nums)
        if i < 0:
            return 0
        if (i, nums[i]) in memo:
            return memo[(i, nums[i])]
        
        ones = sum(1 for j in range(i+1) if nums[j] == 1)
        zeros = sum(1 for j in range(i+1) if nums[j] == 0)

        if ones > 0 and zeros == 0:
            return i + 1
        else:
            res = helper(i-1)
            memo[(i, nums[i])] = res
            return res

    return max(0, helper(len(nums)-1))
