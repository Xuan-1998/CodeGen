def max_bitwise_or(n, s):
    max_or = 0
    for i in range(n):
        for j in range(i + 1, n):
            left_bin = int(s[:i+1], 2)
            right_bin = int(s[i+1:j+1], 2)
            or_val = left_bin | right_bin
            max_or = max(max_or, or_val)
    return bin(max_or)[2:]

n = int(input())
s = input()

print(max_bitwise_or(n, s))
