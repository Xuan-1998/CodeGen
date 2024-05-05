import sys

def max_bitwise_or(s):
    n = len(s)
    max_or = 0

    for i in range(n):  # iterate through all possible substrings
        for j in range(i + 1, n):  # consider non-empty substrings only
            or_val = int(s[i:j+1], 2)  # convert substring to integer and calculate bitwise OR
            max_or = max(max_or, or_val)

    return bin(max_or)[2:]  # print maximum value in binary representation without leading zeroes

n = int(input())
s = input()

print(max_bitwise_or(s))
