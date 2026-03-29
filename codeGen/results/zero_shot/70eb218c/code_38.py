# Read input from standard input
n, x = map(int, input().split())

# Convert integer x to string
x_str = str(x)

# Calculate the current length of decimal representation of x
current_length = len(x_str)

if n < current_length:
    # If it's impossible to make the length equal to n, output -1
    print(-1)
else:
    # Initialize the number of operations
    num_operations = 0

    while current_length < n:
        # Find the last digit in x that is not zero
        for i in range(len(x_str) - 1, -1, -1):
            if x_str[i] != '0':
                break
        else:
            # If all digits are zero, it's impossible to make the length equal to n
            print(-1)
            exit()

        # Multiply x by this digit and update current_length
        num_operations += 1
        x *= int(x_str[i])
        current_length = len(str(x))

    # Output the minimum number of operations
    print(num_operations)
