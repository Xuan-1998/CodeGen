import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

max_or = 0
for i in range(n):
    for j in range(i + 1, n):
        substr1 = s[i:j+1]
        substr2 = s[j:]
        
        val1 = int(substr1, 2)
        val2 = int(substr2, 2)
        
        or_val = val1 | val2
        max_or = max(max_or, or_val)

print(bin(max_or)[2:])
