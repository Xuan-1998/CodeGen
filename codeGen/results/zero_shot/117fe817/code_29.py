import sys

def count_digit_ones(n):
    total_count = 0
    i = 0
    while 10**i <= n:
        interval_count = (10**i - 1) // (9 * 10**(i-1))
        total_count += interval_count
        i += 1
    return total_count

n = int(sys.stdin.readline())
print(count_digit_ones(n))
