code
n = int(input())
blocks = [0] * (n + 1)
binary_str = '0' * n

for i in range(10**n):
    binary_str += format(i, 'b').zfill(n)

count_blocks = 0
curr_digit = None
block_len = 0

for digit in binary_str:
    if digit == curr_digit:
        block_len += 1
    else:
        blocks[block_len] += 1
        count_blocks += 1
        block_len = 1
        curr_digit = digit

blocks[block_len] += 1
print(' '.join(map(str, [block % (998244353) for block in blocks[:n + 1]]))))
