def count_blocks(n):
    block_counts = [0] * (n + 1)
    
    for num in range(10**n):
        num_str = str(num).zfill(n)
        
        curr_digit = num_str[0]
        block_len = 1
        
        for digit in num_str:
            if digit == curr_digit:
                block_len += 1
            else:
                curr_digit = digit
                block_len = 1
        
        block_counts[block_len] = (block_counts[block_len] + 1) % 998244353
    
    return ' '.join(map(str, block_counts))

n = int(input())
print(count_blocks(n))
