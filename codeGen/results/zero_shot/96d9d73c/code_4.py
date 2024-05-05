# Read input from standard input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Sort the array in non-decreasing order
A.sort()

# Initialize a variable to store the minimum possible partition size
min_partition_size = 1

# Iterate through the sorted array to find the minimum possible partition size
for i in range(K - 1):
    if A[i * K + K - 1] - A[i * K] > M:
        min_partition_size = (i + 1) + (A[i * K + K - 1] - A[i * K]) // (M + 1)
        break

# Initialize a variable to store the maximum possible partition size
max_partition_size = len(A)

# If the minimum possible partition size is greater than or equal to K, it's possible to partition the array
if min_partition_size >= K:
    print(True)  # Output: True
else:
    print(False)  # Output: False
