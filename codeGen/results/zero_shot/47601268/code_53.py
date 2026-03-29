import sys

def count_binary_numbers(n):
    count = 0
    for i in range(n + 1):
        bin_str = bin(i)[2:]  # Convert integer to binary string and remove '0b' prefix
        ones_count = 0
        group_ones = False
        for bit in bin_str:
            if bit == '1':
                ones_count += 1
                group_ones = True
            else:
                group_ones = False
            if not group_ones:
                count += 1
    return count

n = int(sys.stdin.readline())
print(count_binary_numbers(n))
