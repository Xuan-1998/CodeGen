def min_operations(n, x):
    num_digits = len(str(x))
    if num_digits == n:
        return 0  # no operations needed
    elif num_digits < n:
        return -1  # impossible to make the length equal to n

    operations = 0
    while num_digits < n:
        digits = str(x)
        max_digit = int(max(digits))
        if max_digit >= 5:  # we can multiply by 10 or 9
            x *= 9
        else:  # we need to multiply by a digit that makes the length increase
            for i in range(1, max_digit + 1):
                new_x = int(str(x) + str(i))
                if len(str(new_x)) >= n:
                    x = new_x
                    break
        num_digits = len(str(x))
        operations += 1

    return operations

n, x = map(int, input().split())
print(min_operations(n, x))
