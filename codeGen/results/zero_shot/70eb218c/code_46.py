def min_operations(n, x):
    initial_len = len(str(x))
    operations = 0
    while initial_len < n:
        for digit in str(x)[1:]:
            new_x = int(digit) * x
            if str(new_x).lstrip('0') != '0':
                x = new_x
                initial_len = len(str(x))
                operations += 1
                break
        else:
            return -1
    return operations

n, x = map(int, input().split())
print(min_operations(n, x))
