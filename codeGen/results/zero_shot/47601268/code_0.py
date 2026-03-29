import sys

def count_non_consecutive(n):
    result = 0
    for i in range(n+1):
        binary = bin(i)[2:]
        has_consecutive_ones = False
        for j in range(len(binary) - 1):
            if binary[j] == '1' and binary[j+1] == '1':
                has_consecutive_ones = True
                break
        if not has_consecutive_ones:
            result += 1
    return result

n = int(sys.stdin.readline())
print(count_non_consecutive(n))
