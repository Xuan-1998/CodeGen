# Read the input
n, x = map(int, input().split())

# Convert the decimal representation of x into a list
decimal_representations = []
while x > 0:
    decimal_representations.append(x % 10)
    x //= 10

# Calculate the length of the current decimal representation
current_length = len(decimal_representations)

# If the length is already equal to n, return 0
if current_length == n:
    print(0)
else:
    # Calculate the difference in lengths
    difference = n - current_length

    # If it's impossible to make the length of decimal representation of x equal to n,
    # because there aren't enough digits to fill up the rest, return -1
    if difference > len(str(10 ** (current_length + 1 - 1))):
        print(-1)
    else:
        # Calculate the minimum number of operations required
        operations = 0
        while difference > 0:
            operations += 1
            decimal_representations.append(0)
            difference -= 1

        print(operations)
