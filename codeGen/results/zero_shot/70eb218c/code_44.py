import sys

def min_operations(n, x):
    # Step 1: Find the current length of x's decimal representation
    x_str = str(x)
    curr_len = len(x_str)

    if curr_len >= n:
        return 0  # No operations needed

    # Step 2-4: Perform operations to reach the target length n
    ops = 0
    while curr_len < n:
        last_digit = int(x_str[-1])  # Get the last digit of x
        x *= last_digit  # Multiply x by the last digit
        x_str = str(x)  # Update the decimal representation of x
        curr_len = len(x_str)
        ops += 1

    return ops if curr_len >= n else -1

n, x = map(int, sys.stdin.readline().split())
print(min_operations(n, x))
