import sys

n = int(input())
s = input()

max_or = 0

for i in range(n):
    for j in range(i+1, n):
        sub1 = s[i:j]
        sub2 = s[j:]
        
        or_val = int(sub1, 2) | int(sub2, 2)
        max_or = max(max_or, or_val)

print(bin(max_or)[2:])
