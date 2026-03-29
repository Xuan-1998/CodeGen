import sys

n = int(sys.stdin.readline())
total_count = 0

for i in range(n+1):
    total_count += bin(i).count('1')

print(total_count)
