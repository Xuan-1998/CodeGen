import sys

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

partition_count = 1

for i in range(1, N):
    if A[i] - A[i-1] >= M or (A[i] - A[i-1]) // M + 1 >= K:
        partition_count += 1

print(partition_count > 1)
