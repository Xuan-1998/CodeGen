import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

ops = 0
for i in range(n-1):
    if arr[i] >= arr[i+1]:
        ops += arr[i] - arr[i+1] + 1
        arr[i+1] = arr[i] + 1

print(ops)
