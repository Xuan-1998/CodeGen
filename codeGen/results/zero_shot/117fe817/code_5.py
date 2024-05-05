import sys

n = int(sys.stdin.readline())

ones_count = 0
for i in range(n+1):
    ones_count += str(i).count('1')

print(ones_count)
