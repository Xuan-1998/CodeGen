def solve(n):
    MOD = 998244353
    res = [0] * (n + 1)
    
    for i in range(10**n):
        num_str = format(i, 'b').zfill(n)
        block_count = 0
        curr_block_len = 0
        
        for digit in num_str:
            if digit == num_str[0]:
                curr_block_len += 1
            else:
                block_count += 1 - curr_block_len
                curr_block_len = 1
        
        block_count += 1 - curr_block_len
        res[block_count % (n + 1)] = (res[block_count % (n + 1)] + 1) % MOD
    
    return ' '.join(map(str, res))[:-1]
