import sys

N, K, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

A.sort()

can_partition = True
partition_end = [0] * (N // K + 1)

for i in range(N):
    if A[i] > M + partition_end[i // K]:
        can_partition = False
        break
    partition_end[i // K] = A[i]

print(can_partition)
