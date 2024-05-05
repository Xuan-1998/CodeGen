import sys

def min_operations(n, x):
    # Convert x to a string to count its digits
    x_str = str(x)
    current_len = len(x_str)

    if current_len >= n:
        return 0

    operations = 0
    while current_len < n:
        # Find the minimum digit y such that x * y has n digits
        for y in range(5, 10):
            new_x = int(str(x) + str(y))
            new_len = len(str(new_x))
            if new_len >= n:
                break
        operations += 1
        x = new_x

    return -1 if current_len != n else operations

n, x = map(int, input().split())
print(min_operations(n, x))
