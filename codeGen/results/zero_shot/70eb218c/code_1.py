code
import sys

def min_operations(n, x):
    # Calculate the current length of decimal representation of x
    current_length = len(str(x))

    # Determine the goal length
    if current_length < n:
        diff = n - current_length
    else:
        return -1  # It's impossible to make the length equal to n

    # Perform the operations
    for _ in range(diff):
        x *= int(str(x)[-1])  # Multiply with the rightmost digit

    return len(str(x))

n, x = map(int, input().split())
print(min_operations(n, x))
