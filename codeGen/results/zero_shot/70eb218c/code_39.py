def solution():
    # Read input from stdin
    n, x = map(int, input().split())

    # Convert decimal representation of x to binary
    bin_x = ''
    while x > 0:
        bin_x = str(x % 2) + bin_x
        x //= 2

    # Calculate the minimum number of operations
    min_ops = -1
    for i in range(len(bin_x)):
        if len(bin_x) <= n:
            min_ops = i
            break

    print(min_ops)
