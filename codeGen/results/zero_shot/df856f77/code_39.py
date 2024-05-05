def min_operations(arr):
    n = len(arr)
    operations = 0

    for i in range(1, n):
        if arr[i] <= arr[i-1]:
            diff = arr[i-1] - arr[i] + 1
            arr[i] += diff
            operations += diff

    return operations

# Read input from stdin
n = int(input())
arr = list(map(int, input().split()))

# Calculate the minimum number of operations
min_ops = min_operations(arr)

# Print the answer to stdout
print(min_ops)
