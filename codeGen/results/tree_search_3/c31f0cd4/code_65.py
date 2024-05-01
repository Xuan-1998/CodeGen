from itertools import combinations

def distinct_sum_set(nums):
    max_sum = sum(nums)
    dp = {0: 1}
    for i in range(len(nums)):
        temp = {}
        for j in range(max_sum + 1):
            if j - nums[i] >= 0 and (j - nums[i]) in dp:
                temp[j] = temp.get(j, 0) + dp[j - nums[i]]
        dp.update(temp)
    return sorted({sum(c): None for c in combinations(nums, r) for r in range(len(nums))}.values())

input()
nums = list(map(int, input().split()))
print(*distinct_sum_set(nums), sep=' ')
