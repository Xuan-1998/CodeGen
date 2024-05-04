import sys

n = int(sys.stdin.readline())

# Generate the list of integers from 0 to 10^n - 1
integers = [str(i).zfill(n) for i in range(2**n)]

# Count the blocks for each integer
blocks = {}
for integer in integers:
    block_count = 1
    prev_digit = integer[0]
    for digit in integer[1:]:
        if digit == prev_digit:
            block_count += 1
        else:
            prev_digit = digit
            block_count = 1
    blocks[block_count] = blocks.get(block_count, 0) + 1

# Calculate the total count modulo 998244353
total_count = [0] * (n + 1)
for length, count in blocks.items():
    total_count[length] = (total_count[length] + count) % 998244353

# Print the answer
print(' '.join(map(str, total_count)))
