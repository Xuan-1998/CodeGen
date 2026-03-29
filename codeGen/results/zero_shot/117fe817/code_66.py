import sys

def count_digit_ones(n):
    total_count = 0
    for i in range(n + 1):
        total_count += i // 2 + (i % 2)
    return total_count

n = int(sys.stdin.readline())
print(count_digit_ones(n))
