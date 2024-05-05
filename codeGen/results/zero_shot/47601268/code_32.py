def has_consecutive_ones(n):
    while n:
        if (n & 1) and ((n >> 1) & 1):
            return True
        n >>= 1
    return False

def count_numbers_without_consecutive_ones(n):
    count = 0
    for i in range(n + 1):
        if not has_consecutive_ones(i):
            count += 1
    return count

n = int(input())
print(count_numbers_without_consecutive_ones(n))
