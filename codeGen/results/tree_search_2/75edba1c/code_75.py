import sys

N, K = map(int, sys.stdin.readline().split())
Arr = list(map(int, sys.stdin.readline().split()))

result = count_subarrays(K, Arr)
print(result)
