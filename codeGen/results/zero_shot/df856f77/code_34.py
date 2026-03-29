import sys

N = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
operations = float('inf')

for i in range(N-1):
    if arr[i] >= arr[i+1]:
        diff = arr[i] - arr[i+1]
        operations = min(operations, diff + 1)

print(operations)
