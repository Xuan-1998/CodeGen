import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

max_value = 0

for i in range(n):
    for j in range(i + 1, n):
        # Calculate the integer value of each substring
        a = int(s[i:j+1], 2)
        b = int(s[j:], 2) if j < n - 1 else 0
        
        # Update the maximum bitwise OR value
        max_value = max(max_value, a | b)

print(format(max_value, 'b').lstrip('0') or '0')
