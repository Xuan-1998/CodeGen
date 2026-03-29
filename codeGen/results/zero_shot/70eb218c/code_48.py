import sys

def min_operations(n, x):
    # Convert x into a string to get its decimal representation
    x_str = str(x)

    # Calculate the current length of the decimal representation of x
    curr_len = len(x_str)

    # Initialize operations to store the minimum number of operations required
    operations = 0

    while curr_len < n:
        # Find the smallest digit y in the decimal representation of x
        for char in x_str:
            if int(char) > 0:
                y = int(char)
                break

        # Update x to be the product of x and y, and increment operations by 1
        x *= y
        operations += 1

        # Update the current length of the decimal representation of x
        curr_len = len(str(x))

    if curr_len == n:
        return operations
    else:
        return -1

n = int(input())
x = int(input())

print(min_operations(n, x))
