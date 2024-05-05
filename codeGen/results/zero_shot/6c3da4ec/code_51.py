import sys

def max_bitwise_or(s):
    n = len(s)
    max_or = 0
    max_ones = 0

    for left in range(n):
        ones = 0
        or_val = 0
        for right in range(left, n):
            if s[right] == '1':
                ones += 1
            or_val |= int(s[left:right+1], 2)
            max_or = max(max_or, or_val)
            max_ones = max(max_ones, ones)

    return bin(max_or)[2:]

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
print(max_bitwise_or(s))
