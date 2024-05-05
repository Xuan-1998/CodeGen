import sys

def has_consecutive_ones(n):
    return bin(n).count('11') > 0

def count_non_negative(n):
    count = 0
    for i in range(n+1):
        if not has_consecutive_ones(i):
            count += 1
    return count

n = int(sys.stdin.readline())
print(count_non_negative(n))
