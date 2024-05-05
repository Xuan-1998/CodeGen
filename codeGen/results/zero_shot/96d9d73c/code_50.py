import sys

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

last_val, num_partitions = A[0], 1

for i in range(1, N):
    if abs(A[i] - last_val) > M:
        last_val, num_partitions = A[i], num_partitions + 1
    else:
        last_val = A[i]

print(num_partitions <= N // K)
