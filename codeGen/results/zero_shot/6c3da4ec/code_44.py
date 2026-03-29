import sys

n = int(sys.stdin.readline().strip())
s = list(sys.stdin.readline().strip())

max_or_value = 0
left = 0
right = n - 1

while left < right:
    or_value = 0
    for i in range(left, right + 1):
        or_value |= int(s[i])
    
    max_or_value = max(max_or_value, or_value)
    
    left += 1
    right -= 1

print(bin(max_or_value)[2:])
