import sys

def count_numbers_without_consecutive_ones(n):
    count = 0
    i = 1
    while i <= n:
        if bin(i).count('1') % 2 == 0:  # Check if binary representation has no consecutive ones
            count += 1
        i *= 2  # Add the next power of two
    return count

n = int(sys.stdin.readline())
print(count_numbers_without_consecutive_ones(n))
