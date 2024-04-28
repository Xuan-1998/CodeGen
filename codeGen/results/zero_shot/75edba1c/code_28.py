import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

count = 0
max_val = max(arr)
for i in range(n):
    if arr[i] > k:
        for j in range(i, n):
            count += (max(arr[i:j+1]) > k)
