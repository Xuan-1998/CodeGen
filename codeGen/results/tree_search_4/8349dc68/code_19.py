import sys

arr = list(map(int, sys.stdin.readline().strip().split()))
k = int(sys.stdin.readline())

print(max_sum_after_partitioning(arr, k))
