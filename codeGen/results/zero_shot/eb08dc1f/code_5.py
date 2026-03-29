n = int(input())
numbers = [str(i).zfill(n) for i in range(10**n)]

def count_blocks(s):
    blocks = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            blocks += 1
    return blocks

block_counts = {}
for s in numbers:
    length = len(s)
    if length not in block_counts:
        block_counts[length] = 0
    block_counts[length] += count_blocks(s)

print(*[block_counts[i] % 998244353 for i in range(1, n+1)], sep=' ')
