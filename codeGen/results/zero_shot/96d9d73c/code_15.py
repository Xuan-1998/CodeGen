import sys

def possible_partition(n, k, m, arr):
    # Sort the array in non-decreasing order
    arr.sort()

    # Initialize the current partition size to 1
    curr_size = 1

    # Iterate through the sorted array
    for i in range(1, n):
        # If the difference between the current element and the previous one exceeds M,
        # or if we've reached K elements in the current partition,
        # start a new partition
        if arr[i] - arr[i-1] > m or curr_size >= k:
            curr_size = 1
        else:
            curr_size += 1

    # Check if the last element can be added to the same partition as the previous one
    if arr[n-1] - arr[0] <= m and curr_size < k:
        return True
    else:
        return False


n, k, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

print(possible_partition(n, k, m, arr))
