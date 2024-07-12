python
def max_remaining_element(n, arr):
    # Iterate through the array from the end to the beginning
    for i in range(n - 1, 0, -1):
        # Always subtract the next element from the current element
        arr[i - 1] = arr[i - 1] - arr[i]
    
    # The remaining element after all operations
    return arr[0]

# Reading input from stdin
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
arr = list(map(int, data[1:]))

# Compute and print the result
print(max_remaining_element(n, arr))

