import sys

# Read input from standard input
n, x = map(int, input().split())

# Define the dictionary to store the results of subproblems
dp = {}

def min_operations(x, n):
    # Base case: if the length of decimal representation of x is equal to n, return 0
    if len(str(x)) == n:
        return 0

    # Check if the result is already stored in the dictionary
    if (x, n) in dp:
        return dp[(x, n)]

    # Transition relationship: try to multiply x by 0-9 and recursively calculate the minimum number of operations required for each possibility
    min_ops = sys.maxsize
    for y in range(10):
        new_x = x * (y if str(x)[0] == '0' else int(str(y) + str(x)))
        ops = min_operations(new_x, n)
        if ops != -1 and len(str(new_x)) < n:
            min_ops = min(min_ops, ops + 1)

    # Store the result in the dictionary
    dp[(x, n)] = -1 if min_ops == sys.maxsize else min_ops

    return dp[(x, n)]

# Print the output to standard output
print(min_operations(x, n))
