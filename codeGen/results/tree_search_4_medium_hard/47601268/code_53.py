import sys

def has_consecutive_ones(n):
    if n == 0:
        return False
    while n > 0:
        remainder = n % 2
        if remainder == 1 and (n // 2) % 2 == 1:
            return True
        n //= 2
    return False

def count_numbers_without_consecutive_ones(n):
    count = 0
    for i in range(n + 1):
        if not has_consecutive_ones(i):
            count += 1
    return count

n = int(sys.stdin.readline())
print(count_numbers_without_consecutive_ones(n))
