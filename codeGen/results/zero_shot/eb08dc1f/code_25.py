import sys

def generate_numbers(n):
    numbers = []
    for i in range(10**n):
        num = format(i, '0{}d'.format(n))
        numbers.append(int(num))
    return numbers

block_counts = {}
for num in generate_numbers(n):
    digit_count = {}
    for digit in str(num):
        if digit not in digit_count:
            digit_count[digit] = 0
        digit_count[digit] += 1

    block_lengths = []
    prev_digit = None
    curr_block_length = 0
    for digit in str(num):
        if digit == prev_digit:
            curr_block_length += 1
        else:
            if prev_digit is not None:
                block_lengths.append(curr_block_length)
            prev_digit = digit
            curr_block_length = 1

    if prev_digit is not None:
        block_lengths.append(curr_block_length)

    for length in set(block_lengths):
        block_counts[length] = (block_counts.get(length, 0) + len([x for x in block_lengths if x == length])) % 998244353

print(*[str(block_counts.get(i, 0)) for i in range(1, n+1)], sep=' ')
