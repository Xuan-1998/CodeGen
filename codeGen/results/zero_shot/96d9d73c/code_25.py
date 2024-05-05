# Read input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Sort the array in ascending order
A.sort()

# Initialize two pointers, one at the start and one at the end of the array
start = 0
end = N - 1

# Loop until the two pointers meet or we find a partition that satisfies the conditions
while start < end:
    # Calculate the absolute difference between the current elements
    diff = abs(A[start] - A[end])

    # If the difference is less than or equal to M, it means we can form a partition with at least K elements
    if diff <= M:
        print("True")  # Return True if possible to partition
        break

    # Move the pointers based on the difference
    if diff > M:
        if A[start] < A[end]:
            start += 1
        else:
            end -= 1

# If we reached this point, it means we couldn't find a partition that satisfies the conditions
print("False")
