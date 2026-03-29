import sys

n = int(sys.stdin.readline())

count = 0
for i in range(n + 1):
    if bin(i).endswith('0'):
        count += 1

print(count)
