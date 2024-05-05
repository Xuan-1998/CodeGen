import sys

def max_bitwise_or(s):
    max_val = 0
    curr_max = 0
    for c in s:
        if c == '1':
            curr_max += 2
        else:
            curr_max = 0
        max_val = max(max_val, curr_max)
    return bin(max_val)[2:]

n = int(input())
s = input()
print(max_bitwise_or(s))
