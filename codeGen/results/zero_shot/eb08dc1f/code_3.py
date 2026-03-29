n = int(input())

integers = [str(i).zfill(n) for i in range(10**n)]

block_counts = {}

for integer in integers:
    block_len = 1
    prev_digit = integer[0]
    for digit in integer[1:]:
        if digit == prev_digit:
            block_len += 1
        else:
            block_counts[block_len] = block_counts.get(block_len, 0) + 1
            block_len = 1
        prev_digit = digit
    # count the last block
    block_counts[block_len] = block_counts.get(block_len, 0) + 1

print(*[block_counts[i] % 998244353 for i in range(1, n+1)], sep=' ')
