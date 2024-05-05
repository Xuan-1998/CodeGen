import sys

def min_operations(arr):
    n = len(arr)
    operations = 0

    for i in range(1, n):
        if arr[i] <= arr[i-1]:
            diff = arr[i-1] - arr[i] + 1
            arr[i:i+1] = [x + j * (diff // j) for j in range(1, diff//j+1)]
            operations += diff

    return operations

# Read input from stdin
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# Calculate the minimum number of operations
min_ops = min_operations(arr)

# Print the output to stdout
print(min_ops)
