import sys

def find_non_consecutive_ones(n):
    count = 0
    for i in range(n+1):
        binary = bin(i)[2:]
        consecutive_count = 0
        consecutive_one = False
        for bit in binary:
            if bit == '1':
                if not consecutive_one:
                    consecutive_one = True
                else:
                    break
            else:
                consecutive_one = False
        else:
            count += 1
    return count

n = int(sys.stdin.readline())
print(find_non_consecutive_ones(n))
