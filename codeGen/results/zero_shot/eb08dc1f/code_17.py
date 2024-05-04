def count_blocks(n):
    MOD = 998244353
    blocks = [0] * (n + 1)
    
    for i in range(10**n):
        s = str(i).zfill(n)
        
        block_len = 1
        prev_digit = s[0]
        
        for j in range(1, n):
            if s[j] == prev_digit:
                block_len += 1
            else:
                blocks[block_len] += 1
                block_len = 1
                prev_digit = s[j]
        
        blocks[block_len] += 1
    
    return ' '.join(str(block) for block in blocks[:n+1])

if __name__ == "__main__":
    n = int(input())
    print(count_blocks(n))
