import sys

def count_no_consecutive_ones(n):
    no_consecutive_ones = 0
    for i in range(n+1):
        has_consecutive_ones = False
        bin_i = bin(i)[2:]  # Convert to binary and remove the '0b' prefix
        for j in range(len(bin_i) - 1):
            if bin_i[j] == '1' and bin_i[j + 1] == '1':
                has_consecutive_ones = True
                break
        if not has_consecutive_ones:
            no_consecutive_ones += 1
    return no_consecutive_ones

n = int(sys.stdin.readline())
print(count_no_consecutive_ones(n))
