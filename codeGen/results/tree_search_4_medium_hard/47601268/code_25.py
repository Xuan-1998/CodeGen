import sys

n = int(sys.stdin.readline())

def has_consecutive_ones(i):
    result = False
    prev_bit_zero = True
    while i > 0:
        bit = (i & 1)
        if not prev_bit_zero and bit == 1:
            result = True
            break
        prev_bit_zero = bit == 0
        i >>= 1
    return not result

result_count = sum(1 for i in range(n + 1) if has_consecutive_ones(i))
print(result_count)
