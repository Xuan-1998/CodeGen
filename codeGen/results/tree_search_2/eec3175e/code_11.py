def find_subset_sum_divisible_by_m(n, m, nums):
    dp = [False] * (m + 1)
    dp[0] = True
    
    for num in nums:
        for i in range(m, -1, -1):
            if i >= num and dp[i - num]:
                dp[i] = True
                break
    
    return 1 if any(dp) else 0

n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(find_subset_sum_divisible_by_m(n, m, nums))
