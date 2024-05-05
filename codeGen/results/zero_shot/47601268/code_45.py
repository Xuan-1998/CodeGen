import sys

def count_binary_representations(n):
    count = 0
    for i in range(n + 1):
        binary Representation = bin(i)[2:]
        prev_bit = None
        consecutive_ones = 0
        for bit in binary_representation:
            if bit == '1' and prev_bit == '1':
                consecutive_ones += 1
            elif consecutive_ones > 0:
                break
            prev_bit = bit
        else:
            count += 1
    return count

n = int(sys.stdin.readline())
print(count_binary_representations(n))
