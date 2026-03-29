def generate_list(n):
    return [str(i).zfill(n) for i in range(10**n)]

def count_blocks(lst):
    block_counts = {}
    for num in lst:
        blocks = []
        block = ''
        for digit in num:
            if digit == block:
                block += digit
            else:
                blocks.append(len(block))
                block = digit
        blocks.append(len(block))
        for length, count in zip(*sorted(set(blocks))):
            block_counts[length] = (block_counts.get(length, 0) + count) % 998244353
    return [block_counts.get(i, 0) for i in range(1, n+1)]

n = int(input())
result = count_blocks(generate_list(n))
print(*result, sep=' ')
