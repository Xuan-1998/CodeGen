import sys

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

max_or_value = 0

for i in range(n):
    for j in range(i+1, n):
        substr1 = s[i:j+1]
        for k in range(j+1, n):
            substr2 = s[j:k+1]
            or_value = int(substr1, 2) | int(substr2, 2)
            max_or_value = max(max_or_value, or_value)

print(bin(max_or_value)[2:])
