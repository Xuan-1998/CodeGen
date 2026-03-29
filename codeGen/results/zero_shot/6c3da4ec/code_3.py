import sys

def max_bitwise_or(s):
    n = len(s)
    max_or = 0

    for i in range(n):
        for j in range(i + 1, n):
            or_value = int(s[i:j+1], 2) | int(s[j:], 2)
            max_or = max(max_or, or_value)

    return bin(max_or)[2:]

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

print(max_bitwise_or(s))
