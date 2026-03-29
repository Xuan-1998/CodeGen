import sys

def count_binary_numbers(n):
    result = 0
    for i in range(2**n + 1):  # Generate all binary numbers from 0 to n
        bin_str = bin(i)[2:]  # Convert integer to binary string, removing '0b' prefix
        has_consecutive_ones = False
        for j in range(len(bin_str) - 1):
            if bin_str[j] == '1' and bin_str[j + 1] == '1':
                has_consecutive_ones = True
                break
        if not has_consecutive_ones:
            result += 1
    return result

n = int(sys.stdin.readline())
print(count_binary_numbers(n))
