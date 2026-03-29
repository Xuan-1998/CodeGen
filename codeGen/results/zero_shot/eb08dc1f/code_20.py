def count_blocks(n):
    mod = 998244353
    counts = {i: 0 for i in range(1, n + 1)}
    
    for num in [str(i).zfill(n) for i in range(10**n)]:
        block_count = 0
        prev_digit = None
        
        for digit in num:
            if digit == prev_digit:
                block_count += 1
            else:
                block_count += 1
                prev_digit = digit
        
        for length, count in counts.items():
            if length <= len(str(block_count)):
                counts[length] = (counts[length] + count) % mod
    
    return ' '.join(map(str, list(counts.values())))

n = int(input())
print(count_blocks(n))
