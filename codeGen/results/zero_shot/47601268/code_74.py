import sys

def count_good_integers(n):
    count = 0
    for i in range(n + 1):
        binary = bin(i)[2:]  # Convert integer to binary and remove the '0b' prefix
        has_consecutive_ones = False
        consecutive_ones_count = 0
        for j in range(len(binary) - 1):
            if binary[j] == '1' and binary[j + 1] == '1':
                consecutive_ones_count += 1
            else:
                consecutive_ones_count = 0
            has_consecutive_ones = has_consecutive_ones or consecutive_ones_count > 0
        if not has_consecutive_ones:
            count += 1
    return count

n = int(sys.stdin.readline())
print(count_good_integers(n))
