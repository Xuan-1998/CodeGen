import sys

# Read input from stdin
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
pivot = int(sys.stdin.readline().strip())

# Modified Quick Sort algorithm for partitioning
def partition(arr, pivot):
    left = []
    middle = [x for x in arr if x == pivot]
    right = []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
    return left + middle + right

# Print the partitioned array to stdout
print(' '.join(map(str, partition(arr, pivot))))
