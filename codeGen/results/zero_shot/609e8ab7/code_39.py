import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
l = []
r = []

for i in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

operations = 0

for i in range(2, n+1):
    if l[i-1][0] > r[i-1][0]:
        operations += (r[i-1][0] - l[i-1][0]) + 1
    else:
        operations += max(r[i-1][1:]) - min(l[i-1][1:])

print(operations)
