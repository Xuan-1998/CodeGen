def max_bitwise_or(s):
    n = len(s)
    max_val = 0
    for i in range(n):
        for j in range(i+1, n):
            val1 = int(s[:i+1], 2)
            val2 = int(s[i+1:j+1], 2)
            or_val = val1 | val2
            max_val = max(max_val, or_val)
    return format(max_val, 'b').lstrip('0') or '0'

n = int(input())
s = input()
print(max_bitwise_or(s))
