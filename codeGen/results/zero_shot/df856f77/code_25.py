import sys

def min_operations(arr):
    arr.sort()
    ops = 0
    prev = float('-inf')  # initialize previous element to negative infinity

    for num in arr:
        if num > prev:  # found a gap!
            ops += 1
        prev = num

    return ops

# Receive input from stdin
n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]

# Print the minimum number of operations to stdout
print(min_operations(arr))
