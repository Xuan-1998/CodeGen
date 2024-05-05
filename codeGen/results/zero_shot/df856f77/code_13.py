import sys

n = int(input())
arr = list(map(int, input().split()))

# Step 1: Sort the array
arr.sort()

ops = 0
for i in range(1, n):
    if arr[i] <= arr[i-1]:
        arr[i-1] += 1
        ops += 1

print(ops)
