import sys

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Sort the array in non-decreasing order
A.sort()

partition_count = 0
current_partition_size = 0

for i in range(N):
    if current_partition_size + A[i] >= K:
        partition_count += 1
        current_partition_size = 0
    current_partition_size += A[i]
    if abs(A[i] - (A[0] + (partition_count * M))) > M:
        break

if current_partition_size >= K and partition_count >= N // K:
    print(True)
else:
    print(False)
