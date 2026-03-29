def can_jump(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] == 0:
            continue
        j = min(i + arr[i], n - 1)
        while i < j:
            if arr[j] > 0:
                return True
            j -= 1
        return False

import sys

# Read the array from standard input
arr = list(map(int, sys.stdin.readline().split()))

# Call the can_jump function and print the result to standard output
print(can_jump(arr))
