def find_sums(nums):
    n = len(nums)
    total_sum = sum(nums)
    dp = [False] * (total_sum + 1)
    dp[0] = True
    for num in nums:
        for i in range(total_sum, num - 1, -1):
            if dp[i - num]:
                dp[i] = True
    return [i for i in range(1, total_sum + 1) if dp[i]]
