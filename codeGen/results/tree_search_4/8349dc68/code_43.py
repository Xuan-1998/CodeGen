import sys

arr = [int(x) for x in sys.stdin.readline().split()]
k = int(sys.stdin.readline())

print(maxSumAfterPartition(arr, k))
