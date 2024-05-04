import sys

n = int(sys.stdin.readline())

num_strs = []
for i in range(10**n):
    num_str = format(i, f"0{n}").zfill(n)
    num_strs.append(num_str)

block_counts = {}
for num_str in num_strs:
    blocks = 1
    block_len = 0
    for digit in num_str:
        if digit == str(int(num_str[0])):
            block_len += 1
        else:
            blocks += 1
            block_len = 1
    block_counts[block_len] = block_counts.get(block_len, 0) + 1

print(*[block_counts[i]%998244353 for i in range(1, n+1)], sep=' ')
