import sys

def find_non_consecutive_ones(n):
    count = 0
    for i in range(n + 1):  # iterate through all possible integers up to n
        has_consecutive_ones = False
        bin_str = bin(i)[2:]  # convert integer to binary string (remove '0b' prefix)
        for j in range(len(bin_str) - 1):
            if bin_str[j] == '1' and bin_str[j + 1] == '1':
                has_consecutive_ones = True
                break
        if not has_consecutive_ones:
            count += 1
    return count

n = int(sys.stdin.readline())
print(find_non_consecutive_ones(n))
