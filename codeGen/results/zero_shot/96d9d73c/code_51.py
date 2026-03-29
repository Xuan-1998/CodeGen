# Read input from standard input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Sort the array A in ascending order
A.sort()

# Initialize two pointers: one at the start of the array and one at the end
left = 0
right = N - 1

# Initialize a variable to keep track of whether it's possible to partition
can_partition = False

while left <= right:
    # If the difference between the current elements is less than or equal to M,
    # then we can add this pair to our partition and move both pointers
    if A[right] - A[left] <= M:
        for i in range(left, right + 1):
            if len(set(A[i:i+K])) > 1:  # Check if there's more than one unique element in the window
                can_partition = True
                break
        left += K
        right -= K
    else:
        # If the difference is greater than M, then we need to move the right pointer until the difference becomes less than or equal to M
        while A[right] - A[left] > M and right > left:
            right -= 1
        if A[right] - A[left] <= M:  # Check again after moving the right pointer
            for i in range(left, right + 1):
                if len(set(A[i:i+K])) > 1:  # Check if there's more than one unique element in the window
                    can_partition = True
                    break
        left += K

print(can_partition)
