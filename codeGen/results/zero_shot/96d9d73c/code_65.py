def can_partition(A, K, M):
    N = len(A)
    if K > N: 
        return False  # If K is greater than the length of array, it's not possible
    A.sort()  # Sort the array in ascending order
    left, right = 0, N-1  # Initialize two pointers for binary search
    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index
        if abs(A[mid] - A[left]) <= M:  # If the absolute difference between the middle and first element is within the limit
            right = mid  # Update the right pointer to search in the left half
        else:
            left = mid + 1  # Update the left pointer to search in the right half
    return True if A[left] - A[0] >= K else False

N, K, M = map(int, input().split())
A = list(map(int, input().split()))
print(can_partition(A, K, M))
