import sys

n = int(input())
arr = list(map(int, input().split()))

ops = 0
prev_val = arr[0]

for val in arr[1:]:
    if val <= prev_val:
        ops += (prev_val - val) + 1
    prev_val = val

print(ops)
