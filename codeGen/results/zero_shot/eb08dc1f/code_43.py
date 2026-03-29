import sys

def count_blocks(n):
    # Initialize the result array with zeros
    res = [0] * (n + 1)

    for i in range(1, n + 1):
        # Iterate over all possible blocks of length i
        for block in range(10**i):
            # Convert the block to a string and count its occurrences
            block_str = str(block).zfill(i)
            res[i] += (block_str == block_str[0] * len(block_str)).count(True)

    return [x % 998244353 for x in res]

n = int(sys.stdin.readline())
print(*count_blocks(n), sep=' ')
