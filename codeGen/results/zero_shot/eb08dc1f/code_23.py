import sys

def solve(n):
    mod = 998244353
    counts = [0] * (n + 1)
    
    for i in range(10**n):
        num_str = format(i, 'b').zfill(n)
        block_len = 1
        block_counts = {}
        
        for digit in num_str:
            if digit not in block_counts:
                block_counts[digit] = 1
            else:
                block_counts[digit] += 1
        
        for length, count in sorted(block_counts.items()):
            counts[length] = (counts[length] + count) % mod
    
    return ' '.join(map(str, counts))

n = int(sys.stdin.readline())
print(solve(n))
