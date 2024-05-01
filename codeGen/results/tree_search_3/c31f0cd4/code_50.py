def distinct_sums(nums):
    nums.sort()
    memo = {(0, False): [0]}
    total_sum = sum(nums)
    
    for i in range(len(nums)):
        current_sum = 0
        can_add = True
        
        for j in range(i+1):
            current_sum += nums[j]
            
            if (current_sum, not can_add) in memo:
                can_add = False
            
            if can_add and (total_sum - current_sum, True) in memo:
                can_add = False
                
        if can_add:
            memo[(current_sum, True)] = sorted([x for x in memo[0][1]] + [current_sum])
        
    return ' '.join(map(str, set([sum(x) for x in memo.values()])))
