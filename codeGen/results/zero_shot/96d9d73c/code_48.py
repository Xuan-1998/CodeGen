# Receive input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Sort the array in ascending order
A.sort()

# Initialize a variable to store whether it is possible to partition
is_possible = True

# Iterate over the array
for i in range(len(A) - K + 1):
    # Check if the current window has at most M difference between any pair of elements
    if max(A[i:i+K]) - min(A[i:i+K]) > M:
        is_possible = False
        break

# Print the result
print(is_possible)
