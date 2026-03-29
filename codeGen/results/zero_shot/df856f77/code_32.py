import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]

ops = 0
prev_val = arr[0]

for i in range(1, n):
    if arr[i] <= prev_val:
        ops += 1
    prev_val = arr[i]

print(ops)
