def count_blocks(n):
    MOD = 998244353
    total_counts = [0] * (n + 1)
    
    for i in range(10**n):
        s = str(i).zfill(n)
        block_count = 0
        block_length = 1
        for j in range(1, n):
            if s[j] == s[j-1]:
                block_length += 1
            else:
                block_count += 1
                block_length = 1
        total_counts[block_length % (n + 1)] = (total_counts[block_length % (n + 1)] + 1) % MOD
    
    return ' '.join(map(str, total_counts))

if __name__ == "__main__":
    n = int(input())
    print(count_blocks(n))
