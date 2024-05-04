import sys

def count_blocks(n):
    MOD = 998244353
    block_counts = [0] * (n + 1)

    def generate_numbers(length):
        for num in range(10 ** length):
            num_str = str(num).zfill(length)
            block_len = 1
            while block_len <= length:
                if all(digit == num_str[0] for digit in num_str[block_len:]):
                    block_counts[block_len] += 1
                    break
                block_len += 1

    generate_numbers(n)

    print(*block_counts, sep=' ')

n = int(sys.stdin.readline())
count_blocks(n)
