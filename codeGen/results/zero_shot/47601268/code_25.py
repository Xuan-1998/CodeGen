import sys

def solution():
    n = int(sys.stdin.readline())

    count = 0
    for i in range(n + 1):
        if no_consecutive_ones(i):
            count += 1

    print(count)

def no_consecutive_ones(num):
    binary = bin(num)[2:]
    prev_bit = '0'
    consecutive_ones = False

    for bit in binary:
        if bit == '1' and not consecutive_ones:
            consecutive_ones = True
        elif bit == '1' and consecutive_ones:
            return False
        elif bit == '0':
            consecutive_ones = False
        prev_bit = bit

    return True

if __name__ == "__main__":
    solution()
