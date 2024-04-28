def can_sum_divisible_by_m(nums, m):
    memo = {0: True}
    
    for num in nums:
        new_memo = {}
        for prev_rem in list(memo.keys()):
            new_rem = (prev_rem + num) % m
            if not new_rem in memo:
                new_memo[new_rem] = memo[prev_rem]
            else:
                new_memo[new_rem] = True
        
        memo.update(new_memo)
    
    return any(rem == 0 for rem in memo.keys())

n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(can_sum_divisible_by_m(nums, m))
