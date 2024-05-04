import sys

n = int(sys.stdin.readline())
count_blocks = [0] * (n + 1)

for i in range(10**n):
    num_str = str(i).zfill(n)
    block_length = 1
    while block_length <= n and len(set(num_str[:block_length])) == 1:
        block_length += 1

    count_blocks[block_length] = (count_blocks[block_length] + 1) % 998244353

print(*count_blocks, sep=' ')
