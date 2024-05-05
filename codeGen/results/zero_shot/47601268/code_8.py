import sys

def count_numbers_without_consecutive_ones(n):
    count = 0
    for i in range(n + 1):
        binary = bin(i)[2:]
        has_consecutive_ones = False
        for j in range(len(binary) - 1):
            if binary[j] == '1' and binary[j + 1] == '1':
                has_consecutive_ones = True
                break
        if not has_consecutive_ones:
            count += 1
    return count

n = int(sys.stdin.readline())
print(count_numbers_without_consecutive_ones(n))
