import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
operations = 0

for i in range(1, n):
    if arr[i] <= arr[i-1]:
        diff = arr[i-1] - arr[i] + 1
        operations += diff
        arr[i] += diff

print(operations)
