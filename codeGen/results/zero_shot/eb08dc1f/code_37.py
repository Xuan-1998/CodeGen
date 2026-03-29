def generate_integers(n):
    integers = []
    for i in range(10**n):
        num_str = format(i, '0{}d'.format(n))
        integers.append(int(num_str))
    return integers

def count_blocks(integers):
    block_counts = {}
    for num in integers:
        digit_str = str(num)
        block_length = 1
        current_digit = digit_str[0]
        block_count = 0
        for digit in digit_str[1:]:
            if digit == current_digit:
                block_length += 1
            else:
                block_counts[block_length] = (block_counts.get(block_length, 0) + 1) % 998244353
                block_length = 1
                current_digit = digit
        block_counts[block_length] = (block_counts.get(block_length, 0) + 1) % 998244353
    return block_counts

def print_counts(block_counts):
    for i in range(1, len(str(10**n - 1)) + 1):
        if i in block_counts:
            print(block_counts[i], end=' ')
        else:
            print(0, end=' ')
    print()

if __name__ == '__main__':
    n = int(input())
    integers = generate_integers(n)
    block_counts = count_blocks(integers)
    print_counts(block_counts)
