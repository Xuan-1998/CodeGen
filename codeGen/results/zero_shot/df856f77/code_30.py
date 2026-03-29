import sys

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

ops = 0
for i in range(n-1):
    if arr[i] >= arr[i+1]:
        ops += (arr[i] - arr[i+1]) + 1

print(ops)
