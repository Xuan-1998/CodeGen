def subset_sum_divisible_by_m(n, m):
    memo = {0: True}
    
    for i in range(1, n+1):
        remainders = {}
        
        for prev_remainder, found in memo.items():
            new_remainder = (prev_remainder + i) % m
            
            if not found:
                continue
                
            remainders[new_remainder] = True
            remainders[prev_remainder] = True
        
        memo.update(remainders)
    
    return memo.get(m, False)

n, m = map(int, input().split())
print(subset_sum_divisible_by_m(n, m))
