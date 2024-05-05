import sys

def count_non_consecutive Ones(n):
    count = 0
    for i in range(n + 1):
        if bin(i)[2:] == '0' * len(bin(i)[2:]):
            count += 1
    return count

n = int(sys.stdin.readline())
print(count_non_consecutive_ones(n))
