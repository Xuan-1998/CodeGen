import sys

n = int(sys.stdin.readline())

blocks = [0] * (n + 1)

for i in range(10**n):
    num_str = format(i, 'b').zfill(n+1)
    block_len = 0
    for j in range(n):
        if block_len == 0 or num_str[j] == num_str[block_len-1]:
            block_len += 1
        else:
            blocks[block_len] += 1
            block_len = 1

blocks[n] += 1

print(*[block % 998244353 for block in blocks], sep=' ')
