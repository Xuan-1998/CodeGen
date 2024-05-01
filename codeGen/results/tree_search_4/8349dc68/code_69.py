import sys

arr = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

print(maxSumAfterPartitioning(arr, k))
