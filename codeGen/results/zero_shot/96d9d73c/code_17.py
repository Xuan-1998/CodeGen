# Receive input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# Sort the array in ascending order
A.sort()

# Initialize two pointers: one at the start and one at the end of the array
left, right = 0, N - 1

# Iterate through the array until the left pointer meets the right pointer
while left < right:
    # If the absolute difference between the elements at the left and right pointers is greater than M,
    # it's not possible to partition the array according to the given rules
    if A[right] - A[left] > M:
        print("False")
        break
    
    # If the current element at the right pointer is less than or equal to the required minimum value (A[K-1]),
    # move the right pointer towards the left
    if A[right] <= A[K-1]:
        right -= 1
    # Otherwise, increment the left pointer and check again
    else:
        left += 1

# If the loop completes without finding a pair with an absolute difference greater than M,
# it's possible to partition the array according to the given rules
else:
    print("True")
