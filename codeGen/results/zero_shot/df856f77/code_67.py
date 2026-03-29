import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

ops = 0
for i in range(len(arr) - 1):
    delta = arr[i+1] - arr[i]
    if delta > 0:
        ops += delta

print(ops)
