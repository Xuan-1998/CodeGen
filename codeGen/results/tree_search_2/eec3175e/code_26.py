def subset_sum_divisible(nums, m):
    dp = {0: True}
    total_sum = 0
    
    for num in nums:
        new_dp = {}
        
        for prev_sum in dp:
            new_sum = (prev_sum + num) % m
            if new_sum not in dp and (new_sum == 0 or dp[prev_sum]):
                new_dp[new_sum] = True
                total_sum += num
        
        dp.update(new_dp)
    
    return int(1) if 0 in dp else 0

n, m = map(int, input().split())
nums = list(map(int, input().split()))

print(subset_sum_divisible(nums, m))
