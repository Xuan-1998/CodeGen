# Step 1: Read the input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Step 2: Sort the array
A.sort()

# Step 3: Initialize variables to track the minimum and maximum values in each partition
min_val = A[0]
max_val = A[0]

# Step 4: Iterate over the array, updating the minimum and maximum values as needed
for i in range(1, N):
    if A[i] - min_val <= M:
        max_val = max(max_val, A[i])
    else:
        # If the current element is more than M away from the previous partition's maximum value,
        # we need to start a new partition
        if i >= K:
            print(True)  # It's possible to partition the array
        else:
            print(False)  # It's not possible to partition the array with at least K elements in each partition
        break

print(any(A[i] - min_val <= M for i in range(N)))
