def min_operations(n, x):
    if len(str(x)) == n:
        return 0

    min_ops = float('inf')
    for digit in range(1, 10):
        new_x = int(str(x) + str(digit))
        ops = min_operations(n, new_x)
        if ops != -1 and ops < min_ops:
            min_ops = ops + 1
    return -1 if min_ops == float('inf') else min_ops
