import sys

def has_consecutive_ones(n):
    bin_str = bin(n)[2:]  # convert to binary string and remove '0b' prefix
    for i in range(len(bin_str) - 1):  # check consecutive ones
        if bin_str[i] == '1' and bin_str[i + 1] == '1':
            return True
    return False

count = 0
for i in range(n + 1):
    if not has_consecutive_ones(i):
        count += 1

print(count)
