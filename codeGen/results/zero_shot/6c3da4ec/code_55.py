import sys

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

max_or_value = 0

left = right = 0
for i in range(n):
    while left <= i < right and (right - left >= 2):  
        max_or_value = max(max_or_value, int(s[left:right+1], 2))  
        left += 1  
    right = i + 1  

print(bin(max_or_value)[2:])  
