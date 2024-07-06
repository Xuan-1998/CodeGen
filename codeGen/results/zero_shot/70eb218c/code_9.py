def min_operations(n, x):
    # Step 1: Calculate the number of digits in x
    num_digits_x = len(str(x))

    if n < num_digits_x:
        return -1  # It's impossible to make the length equal to n

    operations = 0

    while True:
        # Step 2: Find the rightmost digit that is not zero
        i = len(str(x)) - 1
        while i >= 0 and str(x)[i] == '0':
            i -= 1

        if i < 0:
            break  # No more operations needed

        x *= int(str(x)[i])  # Perform the operation
        operations += 1

    return n - num_digits_x + operations
