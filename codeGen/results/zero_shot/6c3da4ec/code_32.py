import sys

def read_input():
    n = int(input())
    s = input()
    return n, s

n, s = read_input()

# Initialize the maximum bitwise OR value
max_or = 0

for i in range(n):
    for j in range(i + 1, n):
        left = int(s[:i+1], 2)
        right = int(s[i+1:j+1], 2)
        or_value = left | right
        max_or = max(max_or, or_value)

print(format(max_or, 'b'))
