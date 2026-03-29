# Read input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Sort the array A
A.sort()

# Initialize a variable to store the maximum possible value in a partition
max_val = 0
for i in range(N):
    if A[i] > max_val + M:
        break
    max_val += M

# Check if it is possible to partition the array into at least K partitions
if max_val >= A[-1] // (K - 1) * (K - 1) and A.count(A[0]) >= K:
    print(True)
else:
    print(False)
