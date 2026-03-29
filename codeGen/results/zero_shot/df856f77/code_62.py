import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

operations = 0
for i in range(n-1):
    if a[i] >= a[i+1]:
        operations += 1

print(operations)
