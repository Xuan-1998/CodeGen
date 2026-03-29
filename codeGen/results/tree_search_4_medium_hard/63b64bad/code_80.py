# Define a dictionary to store the memoized values
memo = {}

def simulate_program(x, y):
    # Base case: if x is out of bounds, return the current value of y
    if x <= 0 or x > n:
        return y

    # Calculate the new state using the sequence value at position x
    a_x = sequence[x-2]  # Note that array indices start from 0
    new_x = x + a_x
    new_y = y + a_x

    # Check if the new state is already in the memo table
    if (new_x, new_y) in memo:
        return memo[(new_x, new_y)]

    # If not, recursively calculate the value of y for the new state
    result = simulate_program(new_x, new_y)

    # Store the calculated value in the memo table
    memo[(new_x, new_y)] = result

    return result

# Read input values from stdin
n = int(input())
sequence = list(map(int, input().split()))

# Initialize the maximum sequence value seen so far
max_sequence_value = 0

for i in range(1, n+1):
    # Run the program and calculate the final value of y
    result = simulate_program(i, 0)

    # Update the maximum sequence value if necessary
    max_sequence_value = max(max_sequence_value, sequence[i-2])

    # Print the result or -1 if the program does not terminate
    print(result) if result <= 10**9 else print(-1)
