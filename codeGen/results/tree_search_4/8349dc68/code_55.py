import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

result = max_sum_after_partitioning(arr, k)
print(result)
