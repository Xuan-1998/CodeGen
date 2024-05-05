import sys

def can_partition(n, k, m, arr):
    # Sort the array in ascending order
    arr.sort()

    for i in range(k-1):
        if arr[i+1] - arr[i] > m:
            return False

    return True

# Read input from stdin
n, k, m = map(int, sys.stdin.readline().split())
arr = [int(x) for x in sys.stdin.readline().split()]

# Call the function and print the result to stdout
print(can_partition(n, k, m, arr))
