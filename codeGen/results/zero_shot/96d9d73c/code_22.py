# Step 1: Read the input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Step 2: Sort the array in ascending order
A.sort()

# Step 3: Initialize a variable to keep track of the number of partitions
partitions = 0

# Step 4: Iterate through the sorted array and form partitions
for i in range(len(A)):
    if i > 0 and A[i] - A[i-1] > M:
        partitions += 1
        if len(A) - i <= K - 1:
            print("True")
            exit()
    if len(A) - i < K:
        print("False")
        exit()

print(partitions + (len(A) % K == 0))
