# Read input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Sort the array in ascending order
A.sort()

# Initialize a variable to store whether it is possible to partition the array
is_possible = False

# Calculate the maximum value that can be the last element of each partition
max_last_element = sum(A) - M * (K - 1)

# Iterate over the array to check if it is possible to partition the array
for i in range(len(A)):
    # If the current element exceeds the maximum allowed value, break the loop
    if A[i] > max_last_element:
        break
    # Update the maximum allowed value for the next partition
    max_last_element -= M

# Print the result
print(is_possible)
